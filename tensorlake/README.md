# Tensorlake benchmark comparison (2026-10-10)

Compares the Tensorlake runs of this fork with runs-on.com's published data.
The raw results stay where the workflows wrote them: `results/<suite>/` on
`main`.

| File | What it is |
|---|---|
| `summary.md` | One table per suite: Tensorlake median and range, rank, GitHub, fastest |
| `full.md` | Every runner per suite and size, plus CPU, memory, disk and burst tables |
| `summary.py`, `compare.py` | Scripts that produce `summary.md` and `full.md` |
| `run-ids.txt` | The workflow runs used, one job per runner per run |
| `runs-on-runners-2026-10-08.json` | runs-on.com's data, from <https://runs-on.com/benchmarks/data/runners.json> on 2026-10-08 |
| `drive2.sh` | The script that dispatched the suites one after another |

`run-ids.txt` leaves out run 38012657130, a first rust pass that ran 9 jobs at
once instead of one job per runner.

To rebuild the tables from the repository root:

```bash
python3 tensorlake/summary.py tensorlake/runs-on-runners-2026-10-08.json results $(cat tensorlake/run-ids.txt) > tensorlake/summary.md
python3 tensorlake/compare.py tensorlake/runs-on-runners-2026-10-08.json results $(cat tensorlake/run-ids.txt) > tensorlake/full.md
```
