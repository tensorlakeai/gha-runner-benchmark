#!/usr/bin/env python3
"""Compare Tensorlake results from the fork with runs-on.com's published data.

Usage: compare.py <their runners.json> <fork results dir> [run ids...]

Medians follow the harness: workload = sum of the timed phases, job = GitHub
job duration, queue = started_at - created_at. Medians use successful jobs.
"""
import glob
import json
import statistics
import sys
from collections import defaultdict

theirs = json.load(open(sys.argv[1]))["suites"]
results_dir = sys.argv[2]
only_runs = set(sys.argv[3:])


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def ours(suite):
    rows = defaultdict(list)
    for f in sorted(glob.glob(f"{results_dir}/{suite}/*.json")):
        d = json.load(open(f))
        if only_runs and str(d["run"]["id"]) not in only_runs:
            continue
        for r in d["results"]:
            if r["provider"] == "Tensorlake":
                rows[r["runnerId"]].append(r)
    out = {}
    for rid, rs in rows.items():
        ok = [r for r in rs if r["status"] == "success"]
        metrics = defaultdict(list)
        for r in ok:
            for k, v in flatten(r.get("metrics") or {}).items():
                if isinstance(v, (int, float)):
                    metrics[k].append(v)
        phases = defaultdict(list)
        for r in ok:
            for p in r.get("phases") or []:
                phases[p["name"]].append(p["seconds"])
        out[rid] = {
            "runnerId": rid, "provider": "Tensorlake", "vcpu": rs[0].get("vcpu"),
            "samples": len(rs), "successes": len(ok),
            "workload": med([r.get("workloadSeconds") for r in ok]),
            "job": med([r.get("jobSeconds") for r in ok]),
            "queue": med([r.get("queueSeconds") for r in ok]),
            "queueP90": pct([r.get("queueSeconds") for r in ok], 0.9),
            "queueMax": max([r.get("queueSeconds") or 0 for r in ok], default=None),
            "phases": {k: med(v) for k, v in phases.items()},
            "metrics": {k: med(v) for k, v in metrics.items()},
            "failures": [(r.get("failedAt"), r.get("reason")) for r in rs if r["status"] != "success"],
        }
    return out


def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            out.update(flatten(v, key + "."))
        else:
            out[key] = v
    return out


def pct(xs, q):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    i = q * (len(xs) - 1)
    lo, hi = int(i), min(int(i) + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (i - lo)


def their_rows(suite, vcpu):
    rows = []
    for r in theirs[suite]["rows"]:
        if r["arch"] != "x64" or r["vcpu"] != vcpu or r.get("successes", 0) == 0:
            continue
        if r["provider"] == "Tensorlake":
            continue
        rows.append({
            "runnerId": r["runnerId"], "provider": r["provider"], "ram": r["ramGiB"],
            "samples": r["samples"], "successes": r["successes"],
            "workload": (r.get("workload") or {}).get("median"),
            "job": r.get("jobSeconds"),
            "queue": (r.get("queue") or {}).get("median"),
            "queueP90": (r.get("queue") or {}).get("p90"),
            "queueMax": (r.get("queue") or {}).get("max"),
            "phases": r.get("phases") or {},
            "metrics": r.get("metrics") or {},
            "perMinute": (r.get("price") or {}).get("perMinute"),
        })
    return rows


def fmt(v, nd=0):
    if v is None:
        return "–"
    return f"{v:,.{nd}f}" if isinstance(v, float) and nd else f"{v:,.0f}" if isinstance(v, (int, float)) else str(v)


SIZES = {"tensorlake-x64-2x8": (2, 8), "tensorlake-x64": (4, 16), "tensorlake-x64-8x32": (8, 32)}


def build_table(suite, title):
    mine = ours(suite)
    print(f"\n## {title}\n")
    for rid, (vcpu, ram) in SIZES.items():
        m = mine.get(rid) or mine.get(f"{rid}.actions-cache")
        rows = their_rows(suite, vcpu)
        if not m and not rows:
            continue
        if m:
            rows.append({**m, "ram": ram, "perMinute": None})
        rows = [r for r in rows if r["workload"] is not None]
        rows.sort(key=lambda r: r["workload"])
        print(f"### {vcpu} vCPU\n")
        print("| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |")
        print("|---:|---|---:|---:|---:|---:|---:|---:|")
        for i, r in enumerate(rows, 1):
            name = f"**{r['runnerId']}**" if r["provider"] == "Tensorlake" else r["runnerId"]
            wj = (r["queue"] + r["job"]) if r["queue"] is not None and r["job"] is not None else None
            print(f"| {i} | {name} | {r['ram']} | {fmt(r['workload'])} | {fmt(r['job'])} | {fmt(r['queue'])} | {fmt(wj)} | {r['successes']}/{r['samples']} |")
        if m and m["failures"]:
            print(f"\nTensorlake failures: {m['failures']}")
        print()


HW_GROUPS = {
    "CPU and memory": [
        ("cpu.passmarkSingle", "PassMark 1T"), ("cpu.passmarkCpuMark", "PassMark CPU"),
        ("cpu.sysbenchSingleEps", "sysbench 1T"), ("cpu.sysbenchMultiEps", "sysbench all"),
        ("cpu.sevenZipMips", "7-Zip MIPS"), ("memory.readMiBps", "Mem read MiB/s"),
    ],
    "Disk, network, Docker, Postgres": [
        ("disk.randRead.iops", "4k QD32 IOPS"), ("disk.randReadQd1.p99us", "4k QD1 p99 us"),
        ("disk.seqRead.MiBps", "Seq read MiB/s"), ("disk.syncWrite.iops", "Sync write IOPS"),
        ("network.githubDownload.MiBps", "GitHub dl MiB/s"), ("docker.pullSeconds", "docker pull s"),
        ("postgres.readWriteTps", "pgbench RW TPS"),
    ],
}


def hardware_table():
    mine = ours("hardware")
    print("\n## Hardware (medians)\n")
    for rid, (vcpu, ram) in SIZES.items():
        rows = their_rows("hardware", vcpu)
        if rid in mine:
            rows.append({**mine[rid], "ram": ram})
        rows = [r for r in rows if r["metrics"]]
        rows.sort(key=lambda r: -(r["metrics"].get("cpu.passmarkSingle") or 0))
        for group, cols in HW_GROUPS.items():
            print(f"### {vcpu} vCPU: {group}\n")
            print("| Runner | RAM | " + " | ".join(n for _, n in cols) + " |")
            print("|---|---:|" + "---:|" * len(cols))
            for r in rows:
                name = f"**{r['runnerId']}**" if r["provider"] == "Tensorlake" else r["runnerId"]
                print(f"| {name} | {r['ram']} | " + " | ".join(fmt(r["metrics"].get(k)) for k, _ in cols) + " |")
            print()


def burst_table():
    mine = ours("burst")
    print("\n## Burst: 15 jobs at once (queue seconds)\n")
    for rid, (vcpu, ram) in SIZES.items():
        rows = their_rows("burst", vcpu)
        if rid in mine:
            rows.append({**mine[rid], "ram": ram})
        rows = [r for r in rows if r["queue"] is not None]
        rows.sort(key=lambda r: r["queue"])
        print(f"### {vcpu} vCPU\n")
        print("| Runner | RAM | Queue p50 | p90 | max | Jobs ok |")
        print("|---|---:|---:|---:|---:|---:|")
        for r in rows:
            name = f"**{r['runnerId']}**" if r["provider"] == "Tensorlake" else r["runnerId"]
            print(f"| {name} | {r['ram']} | {fmt(r['queue'])} | {fmt(r['queueP90'])} | {fmt(r['queueMax'])} | {r['successes']}/{r['samples']} |")
        print()


if __name__ == "__main__":
    for suite, title in (("rust", "Rust: spotify-player"), ("node", "TypeScript: opencode"),
                         ("docker", "Docker: PostHog"), ("cache", "Cache: 4 GB actions/cache")):
        build_table(suite, title)
    hardware_table()
    burst_table()
