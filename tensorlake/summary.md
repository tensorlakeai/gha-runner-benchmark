
### Rust build steps (s, lower is better)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 1,010 | 745–1,111 | 3/3 | 18 of 18 | 401 | 159 (namespace-x64-2x8) |
| 4 vCPU | 632 | 562–704 | 3/3 | 20 of 20 | 227 | 98 (namespace-x64) |
| 8 vCPU | 415 | 103–445 | 3/3 | 20 of 20 | 124 | 71 (namespace-x64-8x32) |

### TypeScript build steps (s)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | failed | – | 0/3 | – | 236 | 98 (runson-m8azn-large) |
| 4 vCPU | 190 | 185–271 | 3/3 | 18 of 18 | 116 | 45 (runson-m8azn-gp3tuned-x64) |
| 8 vCPU | 179 | 169–260 | 3/3 | 19 of 19 | 61 | 29 (runson-m8a-2xlarge-tmpfs) |

### Docker build steps (s)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 4 vCPU | 1,075 | 671–1,197 | 3/3 | 17 of 17 | 770 | 303 (runson-r8a-tmpfs-x64) |
| 8 vCPU | 835 | 528–960 | 3/3 | 20 of 20 | 472 | 224 (runson-r8a-2xlarge-tmpfs-x64) |

### Cache save + restore, 4 GB (s; tmpfs runners not ranked)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 77 | 76–117 | 3/3 | 13 of 18 | 99 | 21 (blacksmith-x64-2x8) |
| 4 vCPU | 79 | 78–116 | 3/3 | 15 of 19 | 57 | 21 (blacksmith-x64) |
| 8 vCPU | 125 | 76–282 | 3/3 | 17 of 18 | 55 | 16 (runson-m8a-2xlarge-gp3tuned) |

### Burst: queue wait p50 with 15 jobs at once (s)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 19 | 13–87 | 15/15 | 13 of 18 | 4 | 4 (github-x64-2x8) |
| 4 vCPU | 14 | 12–17 | 15/15 | 6 of 20 | 4 | 4 (github-x64) |
| 8 vCPU | 21 | 10–90 | 15/15 | 16 of 20 | 80 | 10 (blacksmith-x64-8x32) |

### PassMark single-thread (higher is better)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 2,915 | 1,827–2,925 | 5/5 | 16 of 18 | 2,834 | 4,678 (namespace-x64-2x8) |
| 4 vCPU | 2,921 | 1,697–2,928 | 5/5 | 17 of 20 | 2,381 | 4,693 (namespace-x64-4x8) |
| 8 vCPU | 2,917 | 2,043–2,927 | 5/5 | 17 of 20 | 2,853 | 4,677 (namespace-x64-8x32) |

### PassMark CPU mark, all cores (higher is better)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 5,223 | 3,380–5,414 | 5/5 | 11 of 18 | 3,801 | 8,309 (namespace-x64-2x8) |
| 4 vCPU | 10,226 | 7,046–10,641 | 5/5 | 12 of 20 | 6,131 | 16,219 (namespace-x64-4x8) |
| 8 vCPU | 19,509 | 13,404–20,386 | 5/5 | 13 of 20 | 13,456 | 30,113 (namespace-x64-8x32) |

### Disk 4k read QD1 p99 latency (us, lower is better; tmpfs not ranked)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 832 | 189–2,966 | 5/5 | 14 of 18 | 289 | 13 (namespace-x64-2x8) |
| 4 vCPU | 864 | 194–2,605 | 5/5 | 15 of 19 | 251 | 12 (namespace-x64) |
| 8 vCPU | 848 | 140–2,998 | 5/5 | 15 of 18 | 232 | 12 (namespace-x64-8x16) |

### Disk sync write IOPS (higher is better; tmpfs not ranked)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 1,222 | 1,030–2,742 | 5/5 | 10 of 18 | 4,336 | 18,068 (namespace-x64-2x8) |
| 4 vCPU | 1,101 | 876–2,446 | 5/5 | 11 of 19 | 3,082 | 20,425 (blacksmith-x64) |
| 8 vCPU | 953 | 749–2,230 | 5/5 | 12 of 18 | 3,968 | 19,717 (blacksmith-x64-8x32) |

### Download from GitHub (MiB/s, higher is better)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 83 | 43–155 | 5/5 | 16 of 18 | 94 | 356 (runson-m8id-large) |
| 4 vCPU | 83 | 53–93 | 5/5 | 18 of 20 | 111 | 358 (runson-r8a-tmpfs-x64) |
| 8 vCPU | 63 | 40–100 | 5/5 | 19 of 20 | 98 | 360 (runson-m8id-2xlarge) |

### pgbench read/write TPS (higher is better)

| Size | Tensorlake median | Tensorlake range | Tensorlake runs ok | Rank of runners | GitHub | Fastest |
|---|---:|---:|---:|---|---:|---|
| 2 vCPU | 2,237 | 682–2,754 | 5/5 | 13 of 17 | 1,396 | 5,825 (blacksmith-x64-2x8) |
| 4 vCPU | 3,699 | 945–4,947 | 5/5 | 10 of 19 | 3,134 | 21,543 (runson-r8a-tmpfs-x64) |
| 8 vCPU | 4,248 | 713–6,461 | 5/5 | 11 of 19 | 4,411 | 28,517 (runson-r8a-2xlarge-tmpfs-x64) |
