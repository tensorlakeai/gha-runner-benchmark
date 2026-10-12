#!/usr/bin/env python3
"""One-line-per-suite summary: Tensorlake median and best run vs GitHub and the fastest.

Usage: summary.py <their runners.json> <fork results dir> <run ids...>
"""
import glob
import json
import statistics
import sys

theirs = json.load(open(sys.argv[1]))["suites"]
results_dir = sys.argv[2]
only = set(sys.argv[3:])
SIZES = {2: "tensorlake-x64-2x8", 4: "tensorlake-x64", 8: "tensorlake-x64-8x32"}
GITHUB = {2: "github-x64-2x8", 4: "github-x64", 8: "github-x64-8x32"}


def our_values(suite, rid, field):
    vals = []
    for f in glob.glob(f"{results_dir}/{suite}/*.json"):
        d = json.load(open(f))
        if str(d["run"]["id"]) not in only:
            continue
        for r in d["results"]:
            if r["runnerId"].split(".")[0] == rid and r["status"] == "success":
                vals.append(field(r))
    return [v for v in vals if v is not None]


def their(suite, vcpu, field, no_tmpfs=False):
    rows = []
    for r in theirs[suite]["rows"]:
        if no_tmpfs and r.get("storage") == "tmpfs":
            continue
        if r["arch"] == "x64" and r["vcpu"] == vcpu and r.get("successes") and r["provider"] != "Tensorlake":
            if suite == "cache" and r.get("cacheAction") != "actions/cache":
                continue
            v = field(r)
            if v is not None:
                rows.append((r["runnerId"].replace(".actions-cache", ""), v))
    return rows


def attempts(suite, rid):
    n = ok = 0
    for f in glob.glob(f"{results_dir}/{suite}/*.json"):
        d = json.load(open(f))
        if str(d["run"]["id"]) not in only:
            continue
        for r in d["results"]:
            if r["runnerId"].split(".")[0] == rid:
                n += 1
                ok += r["status"] == "success"
    return ok, n


def line(title, suite, our_field, their_field, lower_better=True, no_tmpfs=False):
    print(f"\n### {title}\n")
    print("| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |")
    print("|---|---:|---:|---:|---|---:|---|")
    for vcpu, rid in SIZES.items():
        ours = our_values(suite, rid, our_field)
        ok, n = attempts(suite, rid)
        if n == 0:
            continue
        rows = their(suite, vcpu, their_field, no_tmpfs)
        gh = dict(rows).get(GITHUB[vcpu])
        top = sorted(rows, key=lambda x: x[1], reverse=not lower_better)[0]
        ghs = f"{gh:,.0f}" if gh is not None else "–"
        if not ours:
            print(f"| {vcpu} vCPU | failed | – | {ok}/{n} | – | {ghs} | {top[1]:,.0f} ({top[0]}) |")
            continue
        med = statistics.median(ours)
        vals = sorted([v for _, v in rows] + [med], reverse=not lower_better)
        rank = vals.index(med) + 1
        print(f"| {vcpu} vCPU | {med:,.0f} | {min(ours):,.0f}–{max(ours):,.0f} | {ok}/{n} | "
              f"{rank} of {len(vals)} | {ghs} | {top[1]:,.0f} ({top[0]}) |")


wl = lambda r: r.get("workloadSeconds")
twl = lambda r: (r.get("workload") or {}).get("median")
line("Rust build steps (s, lower is better)", "rust", wl, twl)
line("TypeScript build steps (s)", "node", wl, twl)
line("Docker build steps (s)", "docker", wl, twl)
line("Cache save + restore, 4 GB (s; tmpfs runners not ranked)", "cache", wl, twl, no_tmpfs=True)
mq = lambda r: r.get("queueSeconds")
tq = lambda r: (r.get("queue") or {}).get("median")
line("Burst: queue wait p50 with 15 jobs at once (s)", "burst", mq, tq)


def metric(path):
    def f(r):
        m = r.get("metrics") or {}
        if path in m:
            return m[path]
        cur = m
        for part in path.split("."):
            cur = (cur or {}).get(part) if isinstance(cur, dict) else None
        return cur
    return f


for key, title, lower in (
    ("cpu.passmarkSingle", "PassMark single-thread (higher is better)", False),
    ("cpu.passmarkCpuMark", "PassMark CPU mark, all cores (higher is better)", False),
    ("disk.randReadQd1.p99us", "Disk 4k read QD1 p99 latency (us, lower is better; tmpfs not ranked)", True),
    ("disk.syncWrite.iops", "Disk sync write IOPS (higher is better; tmpfs not ranked)", False),
    ("network.githubDownload.MiBps", "Download from GitHub (MiB/s, higher is better)", False),
    ("postgres.readWriteTps", "pgbench read/write TPS (higher is better)", False),
):
    line(title, "hardware", metric(key), metric(key), lower_better=lower,
         no_tmpfs=key.startswith("disk."))
