#!/bin/bash
# Dispatch each suite in turn and wait for it to finish.
set -u
REPO=tensorlakeai/gha-runner-benchmark
ALL=tensorlake-x64,tensorlake-x64-8x32,tensorlake-x64-2x8
wait_run() {
  local wf=$1 id=$2 start=$SECONDS s
  while :; do
    s=$(gh run view $id -R $REPO --json status,conclusion --jq '.status+" "+.conclusion' 2>/dev/null || echo "unknown ")
    case "$s" in completed*) break;; esac
    if [ $((SECONDS - start)) -gt 7200 ]; then echo "$(date -u +%H:%M:%S) $wf run $id still $s after 2h, moving on"; return; fi
    sleep 30
  done
  echo "$(date -u +%H:%M:%S) $wf run $id $s"
}
run_suite() {
  local wf=$1 runners=$2 iters=$3
  local before; before=$(gh run list -R $REPO -w $wf -L 1 --json databaseId --jq '.[0].databaseId // 0')
  if [ -n "$iters" ]; then gh workflow run $wf -R $REPO -f runners=$runners -f iterations=$iters
  else gh workflow run $wf -R $REPO -f runners=$runners; fi
  local id=""
  for _ in $(seq 1 30); do
    sleep 5
    id=$(gh run list -R $REPO -w $wf -L 1 --json databaseId --jq '.[0].databaseId // 0')
    [ "$id" != "$before" ] && break
  done
  echo "$(date -u +%H:%M:%S) $wf started run $id"
  local start=$SECONDS
  while :; do
    s=$(gh run view $id -R $REPO --json status,conclusion --jq '.status+" "+.conclusion' 2>/dev/null || echo "unknown ")
    case "$s" in completed*) break;; esac
    if [ $((SECONDS - start)) -gt 7200 ]; then echo "$(date -u +%H:%M:%S) $wf run $id still $s after 2h, moving on"; return; fi
    sleep 30
  done
  echo "$(date -u +%H:%M:%S) $wf run $id $s"
}
echo "$(date -u +%H:%M:%S) waiting for rust.yml run $RUST_RUN"
wait_run rust.yml $RUST_RUN
# Like upstream: one job per runner per run, repeats as separate runs.
for i in 1 2 3; do run_suite rust.yml $ALL 1; done
for i in 1 2 3; do run_suite node.yml $ALL 1; done
for i in 1 2 3; do run_suite docker.yml tensorlake-x64,tensorlake-x64-8x32 1; done
for i in 1 2 3; do run_suite hardware.yml $ALL 1; done
for i in 1 2 3; do run_suite cache.yml $ALL 1; done
run_suite burst.yml $ALL ""
# Burst shards 2 and 3 are started by the previous shard: wait for all three.
start=$SECONDS
while :; do
  st=$(gh run list -R $REPO -w burst.yml -L 10 --json databaseId,status,conclusion --jq '[length, ([.[] | select(.status != "completed")] | length), ([.[] | "\(.databaseId):\(.conclusion)"] | join(","))] | map(tostring) | join(" ")')
  set -- $st
  [ "$1" -ge 3 ] && [ "$2" -eq 0 ] && break
  [ $((SECONDS - start)) -gt 7200 ] && { echo "burst chain still running after 2h: $st"; break; }
  sleep 30
done
echo "$(date -u +%H:%M:%S) burst runs: $3"
echo "$(date -u +%H:%M:%S) ALL DONE"
