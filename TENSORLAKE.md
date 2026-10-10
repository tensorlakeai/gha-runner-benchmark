# Tensorlake runners in this fork

This is a fork of
[runs-on-demo/benchmark-public](https://github.com/runs-on-demo/benchmark-public),
the harness behind [runs-on.com/benchmarks](https://runs-on.com/benchmarks/).
It runs the same suites on Tensorlake GitHub runners, so the results compare
directly with the published ones.

## What differs from upstream

- `config/runners.json` adds three Tensorlake runners, sized like the other
  providers' 2x8, 4x16 and 8x32 machines:

  | id | vCPU | Memory | Disk |
  |---|---:|---:|---:|
  | `tensorlake-x64-2x8` | 2 | 8 GiB | 80 GiB |
  | `tensorlake-x64` | 4 | 16 GiB | 80 GiB |
  | `tensorlake-x64-8x32` | 8 | 32 GiB | 80 GiB |

- `rust.yml` and `hardware.yml` have one extra step, on Tensorlake rows
  only. It points apt at the Ubuntu archive, because the Tensorlake image pins
  apt to a dated `snapshot.ubuntu.com` mirror. The step is not a `phase:`
  step, so it isn't part of the timed phases.
- `hardware.yml` also installs `postgresql-14` on Tensorlake rows, outside
  the timed groups: on Ubuntu 22.04, `postgresql-client` has no `pgbench`.
- Cron schedules are removed. In this fork a scheduled run would start every
  provider's default runners.

The workloads, timing, and result format are the upstream ones.

## Running a suite

Always pass `runners`. An empty `runners` means every provider's runners.

```bash
R=tensorlake-x64,tensorlake-x64-8x32,tensorlake-x64-2x8

# First: check that each label gets a runner.
gh workflow run smoke.yml -R tensorlakeai/gha-runner-benchmark -f runners=$R

gh workflow run rust.yml     -R tensorlakeai/gha-runner-benchmark -f runners=$R -f iterations=3
gh workflow run node.yml     -R tensorlakeai/gha-runner-benchmark -f runners=$R -f iterations=3
gh workflow run hardware.yml -R tensorlakeai/gha-runner-benchmark -f runners=$R -f iterations=3
gh workflow run cache.yml    -R tensorlakeai/gha-runner-benchmark -f runners=$R -f iterations=3
# PostHog needs more than 8 GB, so the docker suite skips 2x8 (as upstream does).
gh workflow run docker.yml   -R tensorlakeai/gha-runner-benchmark \
  -f runners=tensorlake-x64,tensorlake-x64-8x32 -f iterations=3
# Run alone. Each runner gets 15 jobs at once; the three runners go one after another.
gh workflow run burst.yml    -R tensorlakeai/gha-runner-benchmark -f runners=$R
```

Upstream ranks a runner only after 3 finished runs and reports medians.
Don't run two suites at the same time: they would share capacity.

Each run commits `results/<suite>/<date>-<run id>-<attempt>.json`. Compare
with upstream's raw data:
<https://runs-on.com/benchmarks/data/runners.json>.

To pick up upstream harness changes:

```bash
git fetch upstream && git merge upstream/main
```

## Reading the results

- **Queue time includes our runner start.** `queueSeconds` is GitHub's
  `started_at - created_at`. For us it covers webhook delivery, sandbox boot
  and runner registration. The site's default "whole job" view leaves queue
  out, so compare "wait + job" (`queueSeconds + jobSeconds`) and the burst
  suite.
- **Burst needs quota.** 15 jobs at once must fit the namespace's sandbox
  quota, or the queue measures the quota, not scaling.
- **Burst labels are shared.** Upstream gives each RunsOn job its own label, so
  one job can't take another's runner. Our labels can't carry a per-job value.
- **The cache suite measures GitHub's cache service.** `actions/cache` on our
  runners stores in GitHub's cache, so the suite measures our network path to
  it. It doesn't measure the Tensorlake repository cache.
- **Image:** Ubuntu 22.04, x64 only. Other providers use Ubuntu 24.04 or 26,
  and many have arm64 rows. Toolchains are pinned, so builds still compare.
