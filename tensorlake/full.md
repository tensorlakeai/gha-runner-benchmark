
## Rust: spotify-player

### 2 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | namespace-x64-2x8 | 8 | 159 | 165 | 11 | 176 | 5/5 |
| 2 | runson-m8azn-large | 8 | 170 | 180 | 28 | 208 | 5/5 |
| 3 | runson-m8a-large | 8 | 186 | 193 | 31 | 224 | 5/5 |
| 4 | runson-r8a-large | 16 | 186 | 204 | 33 | 237 | 5/5 |
| 5 | runson-c8a-large | 4 | 199 | 211 | 30 | 241 | 5/5 |
| 6 | blacksmith-x64-2x8 | 8 | 201 | 212 | 12 | 224 | 5/5 |
| 7 | avrea-x64-2 | 8 | 226 | 235 | 23 | 258 | 5/5 |
| 8 | warpbuild-x64-2x | 8 | 227 | 234 | 17 | 251 | 5/5 |
| 9 | ubicloud-x64-2 | 8 | 234 | 245 | 23 | 268 | 5/5 |
| 10 | ubicloud-premium-x64-2 | 8 | 273 | 287 | 28 | 315 | 5/5 |
| 11 | runson-m8id-large | 8 | 296 | 305 | 36 | 341 | 5/5 |
| 12 | runson-m8i-large | 8 | 307 | 316 | 36 | 352 | 5/5 |
| 13 | runson-i7i-large | 16 | 318 | 330 | 29 | 359 | 5/5 |
| 14 | runson-m8i-flex-large | 8 | 318 | 330 | 36 | 366 | 5/5 |
| 15 | runson-t8i-medium | 4 | 330 | 346 | 30 | 376 | 5/5 |
| 16 | github-x64-2x8 | 8 | 401 | 410 | 6 | 416 | 5/5 |
| 17 | codebuild-x64-2x3 | 3 | 503 | 525 | 25 | 550 | 5/5 |
| 18 | **tensorlake-x64-2x8** | 8 | 1,010 | 1,027 | 14 | 1,041 | 3/3 |

### 4 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | namespace-x64 | 16 | 98 | 104 | 11 | 115 | 5/5 |
| 2 | namespace-x64-4x8 | 8 | 98 | 105 | 11 | 116 | 5/5 |
| 3 | starsling-x64 | 16 | 110 | 118 | 12 | 130 | 4/5 |
| 4 | runson-m8azn-x64 | 16 | 112 | 121 | 29 | 150 | 5/5 |
| 5 | runson-m8azn-gp3tuned-x64 | 16 | 114 | 122 | 27 | 149 | 5/5 |
| 6 | runson-m8a-x64 | 16 | 117 | 127 | 24 | 151 | 5/5 |
| 7 | blacksmith-x64 | 16 | 119 | 131 | 10 | 141 | 5/5 |
| 8 | runson-c8a-x64-4x8 | 8 | 125 | 136 | 30 | 166 | 5/5 |
| 9 | runson-r8a-tmpfs-x64 | 32 | 126 | 136 | 24 | 160 | 5/5 |
| 10 | avrea-x64 | 16 | 128 | 136 | 22 | 158 | 5/5 |
| 11 | warpbuild-x64 | 16 | 142 | 148 | 18 | 166 | 5/5 |
| 12 | ubicloud-x64 | 16 | 153 | 164 | 24 | 188 | 5/5 |
| 13 | ubicloud-premium-x64 | 16 | 156 | 167 | 23 | 190 | 5/5 |
| 14 | runson-m8i-flex-xlarge | 16 | 176 | 188 | 30 | 218 | 5/5 |
| 15 | runson-m8id-x64 | 16 | 177 | 187 | 33 | 220 | 5/5 |
| 16 | runson-m8i-xlarge | 16 | 179 | 189 | 32 | 221 | 5/5 |
| 17 | runson-i7i-xlarge | 32 | 182 | 191 | 36 | 227 | 5/5 |
| 18 | github-x64 | 16 | 227 | 233 | 7 | 240 | 5/5 |
| 19 | codebuild-x64 | 8 | 281 | 300 | 24 | 324 | 5/5 |
| 20 | **tensorlake-x64** | 16 | 632 | 647 | 15 | 662 | 3/3 |

### 8 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | namespace-x64-8x32 | 32 | 71 | 76 | 11 | 87 | 5/5 |
| 2 | namespace-x64-8x16 | 16 | 74 | 80 | 12 | 92 | 5/5 |
| 3 | starsling-x64-8x32 | 32 | 78 | 87 | 11 | 98 | 5/5 |
| 4 | blacksmith-x64-8x32 | 32 | 81 | 92 | 13 | 105 | 5/5 |
| 5 | avrea-x64-8x32 | 32 | 85 | 92 | 23 | 115 | 5/5 |
| 6 | runson-c8a-x64-8x16 | 16 | 85 | 95 | 27 | 122 | 5/5 |
| 7 | runson-m8a-2xlarge-gp3tuned | 32 | 85 | 95 | 29 | 124 | 5/5 |
| 8 | runson-r8a-2xlarge-tmpfs-x64 | 64 | 86 | 95 | 23 | 118 | 5/5 |
| 9 | runson-m8a-2xlarge | 32 | 87 | 96 | 37 | 133 | 5/5 |
| 10 | runson-m8a-2xlarge-tmpfs | 32 | 88 | 97 | 30 | 127 | 5/5 |
| 11 | warpbuild-x64-8x32 | 32 | 94 | 101 | 15 | 116 | 5/5 |
| 12 | ubicloud-premium-x64-8x32 | 32 | 101 | 111 | 24 | 135 | 5/5 |
| 13 | runson-m8i-2xlarge | 32 | 114 | 127 | 32 | 159 | 5/5 |
| 14 | runson-m8id-2xlarge | 32 | 114 | 124 | 36 | 160 | 5/5 |
| 15 | runson-m8i-flex-2xlarge | 32 | 116 | 129 | 31 | 160 | 5/5 |
| 16 | runson-i7i-2xlarge | 64 | 117 | 129 | 31 | 160 | 5/5 |
| 17 | ubicloud-x64-8x32 | 32 | 119 | 134 | 28 | 162 | 5/5 |
| 18 | github-x64-8x32 | 32 | 124 | 137 | 3 | 140 | 5/5 |
| 19 | codebuild-x64-8x16 | 16 | 185 | 200 | 25 | 225 | 5/5 |
| 20 | **tensorlake-x64-8x32** | 32 | 415 | 429 | 13 | 442 | 3/3 |


## TypeScript: opencode

### 2 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-m8azn-large | 8 | 98 | 126 | 25 | 150 | 2/5 |
| 2 | runson-r8a-large | 16 | 101 | 122 | 28 | 150 | 5/5 |
| 3 | runson-m8a-large | 8 | 102 | 127 | 24 | 150 | 2/5 |
| 4 | blacksmith-x64-2x8 | 8 | 106 | 119 | 18 | 137 | 5/5 |
| 5 | runson-i7i-large | 16 | 143 | 159 | 31 | 190 | 5/5 |
| 6 | runson-m8i-large | 8 | 147 | 180 | 27 | 207 | 3/5 |
| 7 | ubicloud-premium-x64-2 | 8 | 148 | 167 | 23 | 190 | 5/5 |
| 8 | runson-m8i-flex-large | 8 | 160 | 195 | 27 | 222 | 3/5 |
| 9 | warpbuild-x64-2x | 8 | 172 | 183 | 17 | 200 | 5/5 |
| 10 | runson-m8id-large | 8 | 184 | 201 | 32 | 233 | 2/5 |
| 11 | ubicloud-x64-2 | 8 | 195 | 218 | 30 | 248 | 5/5 |
| 12 | github-x64-2x8 | 8 | 236 | 256 | 6 | 262 | 4/5 |

Tensorlake failures: [('typecheck', None), ('typecheck', None), ('typecheck', None)]

### 4 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-m8azn-gp3tuned-x64 | 16 | 45 | 56 | 23 | 79 | 5/5 |
| 2 | runson-r8a-tmpfs-x64 | 32 | 46 | 60 | 28 | 88 | 5/5 |
| 3 | namespace-x64 | 16 | 47 | 55 | 11 | 66 | 5/5 |
| 4 | namespace-x64-4x8 | 8 | 52 | 60 | – | – | 1/5 |
| 5 | starsling-x64 | 16 | 52 | 64 | 18 | 82 | 5/5 |
| 6 | blacksmith-x64 | 16 | 56 | 67 | 15 | 82 | 5/5 |
| 7 | runson-m8azn-x64 | 16 | 57 | 77 | 23 | 100 | 5/5 |
| 8 | runson-m8a-x64 | 16 | 61 | 80 | 25 | 105 | 5/5 |
| 9 | runson-c8a-x64-4x8 | 8 | 66 | 93 | 23 | 116 | 4/5 |
| 10 | runson-i7i-xlarge | 32 | 75 | 90 | 32 | 122 | 5/5 |
| 11 | runson-m8id-x64 | 16 | 80 | 94 | 27 | 121 | 5/5 |
| 12 | runson-m8i-xlarge | 16 | 85 | 106 | 25 | 131 | 5/5 |
| 13 | runson-m8i-flex-xlarge | 16 | 88 | 109 | 27 | 136 | 5/5 |
| 14 | ubicloud-x64 | 16 | 88 | 103 | 29 | 132 | 5/5 |
| 15 | warpbuild-x64 | 16 | 89 | 97 | 18 | 115 | 5/5 |
| 16 | ubicloud-premium-x64 | 16 | 99 | 116 | 25 | 141 | 5/5 |
| 17 | github-x64 | 16 | 116 | 134 | 4 | 138 | 5/5 |
| 18 | **tensorlake-x64** | 16 | 190 | 206 | 15 | 221 | 3/3 |

### 8 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-m8a-2xlarge-tmpfs | 32 | 29 | 43 | 29 | 72 | 5/5 |
| 2 | namespace-x64-8x32 | 32 | 30 | 39 | 11 | 50 | 5/5 |
| 3 | namespace-x64-8x16 | 16 | 31 | 40 | 10 | 50 | 5/5 |
| 4 | runson-r8a-2xlarge-tmpfs-x64 | 64 | 31 | 44 | 25 | 69 | 5/5 |
| 5 | runson-m8a-2xlarge-gp3tuned | 32 | 33 | 46 | 31 | 77 | 5/5 |
| 6 | blacksmith-x64-8x32 | 32 | 36 | 46 | 14 | 60 | 5/5 |
| 7 | starsling-x64-8x32 | 32 | 37 | 47 | 16 | 63 | 5/5 |
| 8 | ubicloud-premium-x64-8x32 | 32 | 43 | 57 | 26 | 83 | 5/5 |
| 9 | runson-m8id-2xlarge | 32 | 44 | 58 | 29 | 87 | 5/5 |
| 10 | warpbuild-x64-8x32 | 32 | 44 | 53 | 14 | 67 | 5/5 |
| 11 | runson-m8a-2xlarge | 32 | 45 | 70 | 26 | 96 | 5/5 |
| 12 | runson-i7i-2xlarge | 64 | 47 | 65 | 36 | 101 | 5/5 |
| 13 | runson-c8a-x64-8x16 | 16 | 48 | 71 | 25 | 96 | 5/5 |
| 14 | runson-m8i-2xlarge | 32 | 58 | 81 | 33 | 114 | 5/5 |
| 15 | runson-m8i-flex-2xlarge | 32 | 58 | 82 | 27 | 109 | 5/5 |
| 16 | github-x64-8x32 | 32 | 61 | 78 | 6 | 84 | 5/5 |
| 17 | ubicloud-x64-8x32 | 32 | 70 | 91 | 26 | 117 | 5/5 |
| 18 | codebuild-x64-8x16 | 16 | 77 | 111 | 30 | 141 | 5/5 |
| 19 | **tensorlake-x64-8x32** | 32 | 179 | 199 | 15 | 214 | 3/3 |


## Docker: PostHog

### 2 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-r8a-large | 16 | 674 | 734 | 24 | 758 | 6/6 |
| 2 | runson-i7i-large | 16 | 892 | 919 | 24 | 944 | 6/6 |

### 4 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-r8a-tmpfs-x64 | 32 | 303 | 320 | 16 | 336 | 3/5 |
| 2 | namespace-x64 | 16 | 304 | 328 | 9 | 338 | 6/6 |
| 3 | blacksmith-x64 | 16 | 320 | 348 | 10 | 358 | 6/6 |
| 4 | starsling-x64 | 16 | 346 | 372 | 12 | 384 | 6/6 |
| 5 | runson-m8azn-gp3tuned-x64 | 16 | 406 | 464 | 24 | 489 | 6/6 |
| 6 | avrea-x64 | 16 | 442 | 472 | 16 | 488 | 6/6 |
| 7 | warpbuild-x64 | 16 | 460 | 484 | 12 | 496 | 6/6 |
| 8 | runson-m8azn-x64 | 16 | 496 | 556 | 23 | 579 | 6/6 |
| 9 | runson-i7i-xlarge | 32 | 504 | 530 | 29 | 559 | 6/6 |
| 10 | runson-m8a-x64 | 16 | 545 | 608 | 24 | 632 | 6/6 |
| 11 | runson-m8id-x64 | 16 | 561 | 594 | 28 | 623 | 6/6 |
| 12 | ubicloud-premium-x64 | 16 | 682 | 718 | 24 | 742 | 6/6 |
| 13 | ubicloud-x64 | 16 | 722 | 757 | 23 | 780 | 6/6 |
| 14 | runson-m8i-xlarge | 16 | 732 | 796 | 28 | 824 | 6/6 |
| 15 | runson-m8i-flex-xlarge | 16 | 736 | 796 | 30 | 826 | 6/6 |
| 16 | github-x64 | 16 | 770 | 876 | 6 | 882 | 6/6 |
| 17 | **tensorlake-x64** | 16 | 1,075 | 1,113 | 13 | 1,126 | 3/3 |

### 8 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-r8a-2xlarge-tmpfs-x64 | 64 | 224 | 240 | 27 | 266 | 6/6 |
| 2 | runson-m8a-2xlarge-tmpfs | 32 | 234 | 253 | 16 | 269 | 3/5 |
| 3 | namespace-x64-8x16 | 16 | 237 | 261 | 10 | 271 | 6/6 |
| 4 | namespace-x64-8x32 | 32 | 238 | 260 | 10 | 270 | 6/6 |
| 5 | blacksmith-x64-8x32 | 32 | 243 | 268 | 12 | 280 | 6/6 |
| 6 | starsling-x64-8x32 | 32 | 261 | 285 | 12 | 296 | 6/6 |
| 7 | runson-m8a-2xlarge-gp3tuned | 32 | 266 | 288 | 24 | 312 | 5/6 |
| 8 | avrea-x64-8x32 | 32 | 289 | 308 | 18 | 326 | 6/6 |
| 9 | warpbuild-x64-8x32 | 32 | 298 | 316 | 13 | 330 | 6/6 |
| 10 | runson-m8a-2xlarge | 32 | 340 | 373 | 26 | 399 | 6/6 |
| 11 | runson-i7i-2xlarge | 64 | 342 | 370 | 29 | 399 | 6/6 |
| 12 | runson-m8id-2xlarge | 32 | 350 | 382 | 30 | 412 | 6/6 |
| 13 | ubicloud-x64-8x32 | 32 | 438 | 473 | 22 | 496 | 6/6 |
| 14 | runson-m8i-2xlarge | 32 | 440 | 472 | 32 | 504 | 5/6 |
| 15 | runson-c8a-x64-8x16 | 16 | 443 | 506 | 24 | 530 | 6/6 |
| 16 | ubicloud-premium-x64-8x32 | 32 | 444 | 477 | 19 | 496 | 6/6 |
| 17 | runson-m8i-flex-2xlarge | 32 | 449 | 481 | 26 | 507 | 6/6 |
| 18 | github-x64-8x32 | 32 | 472 | 586 | 4 | 590 | 6/6 |
| 19 | codebuild-x64-8x16 | 16 | 825 | 858 | 24 | 882 | 5/5 |
| 20 | **tensorlake-x64-8x32** | 32 | 835 | 892 | 14 | 906 | 3/3 |


## Cache: 4 GB actions/cache

### 2 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | blacksmith-x64-2x8.actions-cache | 8 | 21 | 43 | 11 | 54 | 5/5 |
| 2 | avrea-x64-2.actions-cache | 8 | 35 | 52 | 16 | 68 | 5/5 |
| 3 | runson-r8a-large.actions-cache | 16 | 35 | 54 | 26 | 80 | 4/5 |
| 4 | namespace-x64-2x8.actions-cache | 8 | 36 | 54 | 7 | 61 | 5/5 |
| 5 | runson-i7i-large.actions-cache | 16 | 36 | 61 | 28 | 89 | 5/5 |
| 6 | runson-m8a-large.actions-cache | 8 | 41 | 61 | 32 | 93 | 5/5 |
| 7 | runson-m8azn-large.actions-cache | 8 | 41 | 63 | 25 | 88 | 5/5 |
| 8 | runson-m8i-large.actions-cache | 8 | 42 | 65 | 31 | 96 | 5/5 |
| 9 | runson-m8i-flex-large.actions-cache | 8 | 43 | 67 | 36 | 103 | 5/5 |
| 10 | warpbuild-x64-2x.actions-cache | 8 | 51 | 68 | 12 | 80 | 5/5 |
| 11 | runson-c8a-large.actions-cache | 4 | 66 | 87 | 30 | 117 | 5/5 |
| 12 | runson-t8i-medium.actions-cache | 4 | 75 | 100 | 31 | 131 | 5/5 |
| 13 | **tensorlake-x64-2x8.actions-cache** | 8 | 77 | 102 | 10 | 112 | 3/3 |
| 14 | github-x64-2x8.actions-cache | 8 | 99 | 129 | 4 | 133 | 5/5 |
| 15 | runson-m8id-large.actions-cache | 8 | 115 | 162 | 29 | 191 | 5/5 |
| 16 | ubicloud-x64-2.actions-cache | 8 | 137 | 174 | 19 | 193 | 5/5 |
| 17 | ubicloud-premium-x64-2.actions-cache | 8 | 144 | 177 | 23 | 200 | 5/5 |
| 18 | warpbuild-x64-2x.warpbuilds-cache | 8 | 167 | 183 | 14 | 197 | 5/5 |
| 19 | codebuild-x64-2x3.actions-cache | 3 | 208 | 240 | 21 | 261 | 5/5 |

### 4 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-r8a-tmpfs-x64.actions-cache | 32 | 20 | 38 | 24 | 62 | 5/5 |
| 2 | blacksmith-x64.actions-cache | 16 | 21 | 40 | 11 | 51 | 5/5 |
| 3 | runson-i7i-xlarge.actions-cache | 32 | 23 | 45 | 26 | 71 | 5/5 |
| 4 | runson-m8azn-gp3tuned-x64.actions-cache | 16 | 23 | 39 | 29 | 68 | 5/5 |
| 5 | runson-m8i-xlarge.actions-cache | 16 | 32 | 56 | 34 | 90 | 5/5 |
| 6 | runson-m8azn-x64.actions-cache | 16 | 34 | 53 | 22 | 75 | 5/5 |
| 7 | runson-m8i-flex-xlarge.actions-cache | 16 | 34 | 57 | 33 | 90 | 5/5 |
| 8 | namespace-x64-4x8.actions-cache | 8 | 35 | 52 | 6 | 58 | 5/5 |
| 9 | namespace-x64.actions-cache | 16 | 35 | 53 | 8 | 61 | 5/5 |
| 10 | avrea-x64.actions-cache | 16 | 36 | 53 | 18 | 71 | 5/5 |
| 11 | runson-m8a-x64.actions-cache | 16 | 36 | 55 | 21 | 76 | 8/8 |
| 12 | runson-c8a-x64-4x8.actions-cache | 8 | 40 | 60 | 23 | 83 | 5/5 |
| 13 | runson-m8id-x64.actions-cache | 16 | 56 | 82 | 28 | 110 | 5/5 |
| 14 | github-x64.actions-cache | 16 | 57 | 82 | 3 | 85 | 5/5 |
| 15 | warpbuild-x64.actions-cache | 16 | 66 | 81 | 11 | 92 | 5/5 |
| 16 | **tensorlake-x64.actions-cache** | 16 | 79 | 107 | 10 | 117 | 3/3 |
| 17 | starsling-x64.actions-cache | 16 | 108 | 128 | 8 | 136 | 5/5 |
| 18 | ubicloud-premium-x64.actions-cache | 16 | 122 | 149 | 23 | 172 | 5/5 |
| 19 | ubicloud-x64.actions-cache | 16 | 134 | 166 | 25 | 191 | 5/5 |
| 20 | warpbuild-x64.warpbuilds-cache | 16 | 156 | 172 | 21 | 193 | 5/5 |
| 21 | codebuild-x64.actions-cache | 8 | 182 | 212 | 20 | 232 | 5/5 |

### 8 vCPU

| # | Runner | RAM | Build steps (s) | Whole job (s) | Queue (s) | Wait + job (s) | Runs ok |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | runson-m8a-2xlarge-tmpfs.actions-cache | 32 | 14 | 32 | 29 | 61 | 5/5 |
| 2 | runson-m8a-2xlarge-gp3tuned.actions-cache | 32 | 16 | 34 | 32 | 66 | 5/5 |
| 3 | runson-i7i-2xlarge.actions-cache | 64 | 19 | 41 | 33 | 74 | 5/5 |
| 4 | runson-r8a-2xlarge-tmpfs-x64.actions-cache | 64 | 19 | 37 | 21 | 58 | 5/5 |
| 5 | blacksmith-x64-8x32.actions-cache | 32 | 20 | 39 | 10 | 49 | 5/5 |
| 6 | runson-m8id-2xlarge.actions-cache | 32 | 25 | 47 | 24 | 71 | 5/5 |
| 7 | runson-m8i-2xlarge.actions-cache | 32 | 27 | 51 | 31 | 82 | 5/5 |
| 8 | runson-m8i-flex-2xlarge.actions-cache | 32 | 28 | 51 | 31 | 82 | 5/5 |
| 9 | runson-m8a-2xlarge.actions-cache | 32 | 30 | 48 | 25 | 73 | 5/5 |
| 10 | namespace-x64-8x32.actions-cache | 32 | 33 | 50 | 7 | 57 | 5/5 |
| 11 | namespace-x64-8x16.actions-cache | 16 | 34 | 51 | 7 | 58 | 5/5 |
| 12 | runson-c8a-x64-8x16.actions-cache | 16 | 34 | 53 | 28 | 81 | 5/5 |
| 13 | avrea-x64-8x32.actions-cache | 32 | 36 | 53 | 18 | 71 | 5/5 |
| 14 | warpbuild-x64-8x32.actions-cache | 32 | 45 | 58 | 10 | 68 | 5/5 |
| 15 | github-x64-8x32.actions-cache | 32 | 55 | 80 | 3 | 83 | 5/5 |
| 16 | starsling-x64-8x32.actions-cache | 32 | 78 | 100 | 8 | 108 | 5/5 |
| 17 | ubicloud-premium-x64-8x32.actions-cache | 32 | 120 | 144 | 18 | 162 | 4/5 |
| 18 | ubicloud-x64-8x32.actions-cache | 32 | 120 | 149 | 25 | 174 | 5/5 |
| 19 | **tensorlake-x64-8x32.actions-cache** | 32 | 125 | 153 | 10 | 163 | 3/3 |
| 20 | warpbuild-x64-8x32.warpbuilds-cache | 32 | 158 | 173 | 12 | 185 | 4/5 |
| 21 | codebuild-x64-8x16.actions-cache | 16 | 172 | 204 | 20 | 224 | 5/5 |


## Hardware (medians)

### 2 vCPU: CPU and memory

| Runner | RAM | PassMark 1T | PassMark CPU | sysbench 1T | sysbench all | 7-Zip MIPS | Mem read MiB/s |
|---|---:|---:|---:|---:|---:|---:|---:|
| namespace-x64-2x8 | 8 | 4,678 | 8,309 | 7,007 | 13,714 | 17,627 | 23,454 |
| runson-m8azn-large | 8 | 4,253 | 7,722 | 5,642 | 11,323 | 22,087 | 21,217 |
| avrea-x64-2 | 8 | 4,189 | 5,621 | 6,215 | 6,542 | 12,713 | 18,066 |
| warpbuild-x64-2x | 8 | 4,144 | 5,497 | 6,109 | 6,466 | 12,433 | 18,718 |
| blacksmith-x64-2x8 | 8 | 3,997 | 6,942 | 5,657 | 11,181 | 13,504 | 15,350 |
| runson-c8a-large | 4 | 3,802 | 6,874 | 5,026 | 10,123 | 19,537 | 18,840 |
| runson-m8a-large | 8 | 3,796 | 6,878 | 5,070 | 10,098 | 19,961 | 18,896 |
| runson-r8a-large | 16 | 3,790 | 6,887 | 5,086 | 10,116 | 19,914 | 18,954 |
| ubicloud-premium-x64-2 | 8 | 3,342 | 5,610 | 4,779 | 8,019 | 11,522 | 16,468 |
| runson-m8i-flex-large | 8 | 3,248 | 4,066 | 3,079 | 3,213 | 11,851 | 13,913 |
| runson-t8i-medium | 4 | 3,243 | 4,063 | 3,080 | 3,214 | 11,712 | 13,894 |
| runson-m8id-large | 8 | 3,234 | 4,066 | 3,070 | 3,203 | 11,866 | 13,796 |
| runson-m8i-large | 8 | 3,229 | 4,062 | 3,064 | 3,196 | 11,855 | 13,773 |
| runson-i7i-large | 16 | 3,054 | 3,913 | 3,091 | 3,152 | 11,993 | 12,698 |
| ubicloud-x64-2 | 8 | 2,917 | 5,420 | 4,572 | 9,054 | 13,584 | 16,326 |
| **tensorlake-x64-2x8** | 8 | 2,915 | 5,223 | 4,175 | 7,829 | 7,999 | 11,728 |
| github-x64-2x8 | 8 | 2,834 | 3,801 | 4,516 | 4,767 | 9,906 | 14,137 |
| codebuild-x64-2x3 | 3 | 1,974 | 2,258 | 1,159 | 1,809 | 6,317 | 9,724 |

### 2 vCPU: Disk, network, Docker, Postgres

| Runner | RAM | 4k QD32 IOPS | 4k QD1 p99 us | Seq read MiB/s | Sync write IOPS | GitHub dl MiB/s | docker pull s | pgbench RW TPS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| namespace-x64-2x8 | 8 | 351,146 | 13 | 4,222 | 18,068 | 170 | 5 | 4,368 |
| runson-m8azn-large | 8 | 2,994 | 881 | 401 | 542 | 249 | 5 | 3,093 |
| avrea-x64-2 | 8 | 454,466 | 17 | 8,598 | 8,163 | 128 | 8 | 2,591 |
| warpbuild-x64-2x | 8 | 176,232 | 59 | 7,652 | 2,056 | 176 | 14 | 1,510 |
| blacksmith-x64-2x8 | 8 | 637,720 | 18 | 6,482 | 17,882 | 102 | 9 | 5,825 |
| runson-c8a-large | 4 | 2,994 | 807 | 401 | 541 | 178 | 5 | 2,827 |
| runson-m8a-large | 8 | 2,994 | 774 | 401 | 541 | 247 | 5 | 3,052 |
| runson-r8a-large | 16 | 2,994 | 807 | 401 | 541 | 254 | 5 | 3,218 |
| ubicloud-premium-x64-2 | 8 | 147,821 | 1,106 | 2,734 | 2,417 | 54 | 15 | 1,554 |
| runson-m8i-flex-large | 8 | 2,994 | 881 | 401 | 530 | 323 | 7 | 2,413 |
| runson-t8i-medium | 4 | 3,000 | 790 | 401 | 526 | 270 | 8 | 2,324 |
| runson-m8id-large | 8 | 33,542 | 228 | 226 | 5,549 | 356 | 7 | 3,187 |
| runson-m8i-large | 8 | 2,992 | 872 | 401 | 534 | 240 | 7 | 2,422 |
| runson-i7i-large | 16 | 75,023 | 220 | 503 | 13,514 | 225 | 7 | 3,745 |
| ubicloud-x64-2 | 8 | 112,843 | 807 | 2,731 | 1,870 | 58 | 15 | 1,442 |
| **tensorlake-x64-2x8** | 8 | 201,619 | 832 | 13,965 | 1,222 | 83 | 13 | 2,237 |
| github-x64-2x8 | 8 | 9,374 | 289 | 199 | 4,336 | 94 | 24 | 1,396 |
| codebuild-x64-2x3 | 3 | 2,988 | 823 | 252 | 562 | 178 | 17 | – |

### 4 vCPU: CPU and memory

| Runner | RAM | PassMark 1T | PassMark CPU | sysbench 1T | sysbench all | 7-Zip MIPS | Mem read MiB/s |
|---|---:|---:|---:|---:|---:|---:|---:|
| namespace-x64-4x8 | 8 | 4,693 | 16,219 | 7,031 | 27,548 | 33,225 | 46,345 |
| namespace-x64 | 16 | 4,683 | 16,165 | 7,047 | 27,538 | 33,234 | 45,825 |
| blacksmith-x64 | 16 | 4,357 | 15,469 | 6,511 | 25,924 | 29,630 | 30,532 |
| runson-m8azn-x64 | 16 | 4,264 | 15,141 | 5,689 | 22,784 | 42,503 | 41,852 |
| runson-m8azn-gp3tuned-x64 | 16 | 4,257 | 15,102 | 5,631 | 22,610 | 42,405 | 42,291 |
| warpbuild-x64 | 16 | 4,201 | 11,017 | 6,288 | 13,080 | 23,058 | 37,116 |
| avrea-x64 | 16 | 4,031 | 11,174 | 6,113 | 13,142 | 23,093 | 36,248 |
| runson-m8a-x64 | 16 | 3,807 | 13,471 | 5,048 | 20,243 | 38,732 | 37,352 |
| runson-r8a-tmpfs-x64 | 32 | 3,803 | 13,460 | 5,044 | 20,240 | 38,874 | 37,227 |
| runson-c8a-x64-4x8 | 8 | 3,801 | 13,452 | 5,042 | 20,294 | 39,267 | 37,434 |
| starsling-x64 | 16 | 3,755 | 13,127 | 5,487 | 21,685 | 28,501 | 21,383 |
| runson-m8i-flex-xlarge | 16 | 3,271 | 8,025 | 3,083 | 6,425 | 23,136 | 22,159 |
| runson-m8id-x64 | 16 | 3,266 | 8,054 | 3,079 | 6,421 | 24,326 | 22,260 |
| runson-m8i-xlarge | 16 | 3,256 | 7,989 | 3,078 | 6,412 | 23,345 | 22,186 |
| runson-i7i-xlarge | 32 | 3,105 | 7,745 | 3,053 | 6,190 | 22,329 | 20,525 |
| ubicloud-premium-x64 | 16 | 2,993 | 8,241 | 5,515 | 16,482 | 19,076 | 22,110 |
| **tensorlake-x64** | 16 | 2,921 | 10,226 | 4,084 | 15,795 | 15,145 | 20,156 |
| ubicloud-x64 | 16 | 2,878 | 10,170 | 4,532 | 14,905 | 23,200 | 21,947 |
| github-x64 | 16 | 2,381 | 6,131 | 3,538 | 7,400 | 16,468 | 21,396 |
| codebuild-x64 | 8 | 2,031 | 4,472 | 1,164 | 3,625 | 12,348 | 17,496 |

### 4 vCPU: Disk, network, Docker, Postgres

| Runner | RAM | 4k QD32 IOPS | 4k QD1 p99 us | Seq read MiB/s | Sync write IOPS | GitHub dl MiB/s | docker pull s | pgbench RW TPS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| namespace-x64-4x8 | 8 | 1,015,510 | 13 | 4,245 | 18,087 | 162 | 4 | 8,498 |
| namespace-x64 | 16 | 1,007,328 | 12 | 4,229 | 17,773 | 127 | 4 | 8,424 |
| blacksmith-x64 | 16 | 856,257 | 14 | 6,616 | 20,425 | 107 | 7 | 12,543 |
| runson-m8azn-x64 | 16 | 2,994 | 897 | 401 | 541 | 318 | 5 | 3,334 |
| runson-m8azn-gp3tuned-x64 | 16 | 15,994 | 872 | 1,001 | 539 | 278 | 5 | 3,785 |
| warpbuild-x64 | 16 | 124,074 | 64 | 7,324 | 1,987 | 202 | 12 | 2,717 |
| avrea-x64 | 16 | 468,080 | 18 | 6,739 | 8,648 | 86 | 6 | 5,102 |
| runson-m8a-x64 | 16 | 2,994 | 799 | 401 | 540 | 332 | 5 | 3,257 |
| runson-r8a-tmpfs-x64 | 32 | 4,113,746 | 0 | 18,647 | 431,794 | 358 | 5 | 21,543 |
| runson-c8a-x64-4x8 | 8 | 2,994 | 832 | 401 | 540 | 256 | 5 | 3,087 |
| starsling-x64 | 16 | 262,205 | 17 | 3,993 | 3,385 | 143 | 8 | 7,234 |
| runson-m8i-flex-xlarge | 16 | 2,994 | 774 | 401 | 527 | 224 | 6 | 3,061 |
| runson-m8id-x64 | 16 | 67,089 | 218 | 451 | 7,898 | 221 | 6 | 7,227 |
| runson-m8i-xlarge | 16 | 2,992 | 930 | 401 | 521 | 350 | 6 | 3,149 |
| runson-i7i-xlarge | 32 | 150,053 | 301 | 1,010 | 12,299 | 235 | 7 | 7,018 |
| ubicloud-premium-x64 | 16 | 173,146 | 1,679 | 2,522 | 1,395 | 50 | 17 | 2,151 |
| **tensorlake-x64** | 16 | 274,565 | 864 | 15,058 | 1,101 | 83 | 10 | 3,699 |
| ubicloud-x64 | 16 | 183,661 | 700 | 2,440 | 578 | 63 | 26 | 1,765 |
| github-x64 | 16 | 19,578 | 251 | 394 | 3,082 | 111 | 16 | 3,134 |
| codebuild-x64 | 8 | 2,989 | 758 | 252 | 559 | 221 | 14 | – |

### 8 vCPU: CPU and memory

| Runner | RAM | PassMark 1T | PassMark CPU | sysbench 1T | sysbench all | 7-Zip MIPS | Mem read MiB/s |
|---|---:|---:|---:|---:|---:|---:|---:|
| namespace-x64-8x32 | 32 | 4,677 | 30,113 | 7,023 | 54,158 | 60,979 | 86,023 |
| namespace-x64-8x16 | 16 | 4,641 | 29,377 | 7,023 | 53,373 | 60,156 | 84,952 |
| avrea-x64-8x32 | 32 | 4,273 | 21,356 | 6,212 | 26,414 | 49,101 | 68,267 |
| blacksmith-x64-8x32 | 32 | 4,234 | 27,282 | 6,236 | 49,224 | 55,188 | 48,970 |
| warpbuild-x64-8x32 | 32 | 4,177 | 20,979 | 6,361 | 26,319 | 44,987 | 52,200 |
| starsling-x64-8x32 | 32 | 3,967 | 26,285 | 5,857 | 45,396 | 54,729 | 39,438 |
| runson-r8a-2xlarge-tmpfs-x64 | 64 | 3,818 | 25,489 | 5,052 | 40,313 | 73,980 | 72,704 |
| runson-c8a-x64-8x16 | 16 | 3,818 | 25,489 | 5,045 | 40,355 | 74,021 | 72,862 |
| runson-m8a-2xlarge-tmpfs | 32 | 3,816 | 25,504 | 5,053 | 40,364 | 73,775 | 73,016 |
| runson-m8a-2xlarge | 32 | 3,801 | 25,448 | 5,041 | 40,165 | 73,764 | 72,992 |
| runson-m8a-2xlarge-gp3tuned | 32 | 3,799 | 25,408 | 5,054 | 40,343 | 73,826 | 72,616 |
| ubicloud-premium-x64-8x32 | 32 | 3,517 | 23,407 | 5,971 | 42,525 | 50,188 | 43,680 |
| runson-m8i-flex-2xlarge | 32 | 3,273 | 15,592 | 3,084 | 12,882 | 45,886 | 37,368 |
| runson-m8id-2xlarge | 32 | 3,267 | 15,541 | 3,080 | 12,848 | 47,077 | 36,941 |
| runson-m8i-2xlarge | 32 | 3,258 | 15,482 | 3,074 | 12,821 | 46,156 | 38,042 |
| runson-i7i-2xlarge | 64 | 3,021 | 14,381 | 3,068 | 11,644 | 38,923 | 37,242 |
| **tensorlake-x64-8x32** | 32 | 2,917 | 19,509 | 4,148 | 32,231 | 28,780 | 36,567 |
| github-x64-8x32 | 32 | 2,853 | 13,456 | 3,677 | 16,402 | 32,174 | 42,351 |
| ubicloud-x64-8x32 | 32 | 2,553 | 14,203 | 3,906 | 23,251 | 27,883 | 26,952 |
| codebuild-x64-8x16 | 16 | 2,041 | 8,637 | 1,168 | 7,268 | 23,677 | 32,985 |

### 8 vCPU: Disk, network, Docker, Postgres

| Runner | RAM | 4k QD32 IOPS | 4k QD1 p99 us | Seq read MiB/s | Sync write IOPS | GitHub dl MiB/s | docker pull s | pgbench RW TPS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| namespace-x64-8x32 | 32 | 1,108,356 | 12 | 4,259 | 18,160 | 210 | 4 | 12,119 |
| namespace-x64-8x16 | 16 | 1,120,671 | 12 | 4,193 | 17,740 | 201 | 4 | 11,892 |
| avrea-x64-8x32 | 32 | 235,683 | 19 | 7,607 | 7,570 | 160 | 5 | 7,530 |
| blacksmith-x64-8x32 | 32 | 683,187 | 13 | 6,694 | 19,717 | 123 | 8 | 15,685 |
| warpbuild-x64-8x32 | 32 | 120,520 | 60 | 7,982 | 1,918 | 184 | 11 | 4,181 |
| starsling-x64-8x32 | 32 | 318,790 | 17 | 2,378 | 2,812 | 118 | 7 | 8,363 |
| runson-r8a-2xlarge-tmpfs-x64 | 64 | 4,231,165 | 0 | 19,081 | 433,632 | 196 | 5 | 28,517 |
| runson-c8a-x64-8x16 | 16 | 2,995 | 840 | 401 | 539 | 323 | 5 | 3,266 |
| runson-m8a-2xlarge-tmpfs | 32 | 4,258,470 | 0 | 18,549 | 432,491 | 218 | 5 | 27,991 |
| runson-m8a-2xlarge | 32 | 2,994 | 897 | 401 | 538 | 330 | 5 | 3,290 |
| runson-m8a-2xlarge-gp3tuned | 32 | 15,996 | 840 | 1,001 | 539 | 195 | 5 | 3,751 |
| ubicloud-premium-x64-8x32 | 32 | 374,058 | 305 | 3,544 | 4,203 | 64 | 10 | 3,171 |
| runson-m8i-flex-2xlarge | 32 | 2,992 | 872 | 401 | 520 | 277 | 6 | 3,145 |
| runson-m8id-2xlarge | 32 | 134,258 | 228 | 905 | 7,657 | 360 | 6 | 10,357 |
| runson-m8i-2xlarge | 32 | 2,993 | 1,012 | 401 | 498 | 217 | 6 | 3,188 |
| runson-i7i-2xlarge | 64 | 300,466 | 228 | 2,035 | 11,801 | 249 | 8 | 9,833 |
| **tensorlake-x64-8x32** | 32 | 243,441 | 848 | 18,568 | 953 | 63 | 15 | 4,248 |
| github-x64-8x32 | 32 | 38,940 | 232 | 784 | 3,968 | 98 | 13 | 4,411 |
| ubicloud-x64-8x32 | 32 | 251,230 | 528 | 2,484 | 1,423 | 17 | 21 | 1,800 |
| codebuild-x64-8x16 | 16 | 2,992 | 815 | 252 | 559 | 225 | 12 | – |


## Burst: 15 jobs at once (queue seconds)

### 2 vCPU

| Runner | RAM | Queue p50 | p90 | max | Jobs ok |
|---|---:|---:|---:|---:|---:|
| github-x64-2x8 | 8 | 4 | 5 | 40 | 75/75 |
| blacksmith-x64-2x8 | 8 | 10 | 13 | 14 | 75/75 |
| avrea-x64-2 | 8 | 12 | 16 | 19 | 75/75 |
| warpbuild-x64-2x | 8 | 12 | 14 | 28 | 75/75 |
| runson-c8a-large | 4 | 17 | 20 | 70 | 60/60 |
| runson-m8azn-large | 8 | 17 | 19 | 21 | 60/60 |
| namespace-x64-2x8 | 8 | 18 | 22 | 24 | 15/15 |
| runson-m8a-large | 8 | 18 | 45 | 50 | 60/60 |
| runson-m8i-flex-large | 8 | 18 | 25 | 30 | 60/60 |
| runson-r8a-large | 16 | 18 | 23 | 57 | 60/60 |
| runson-t8i-medium | 4 | 18 | 22 | 57 | 60/60 |
| ubicloud-premium-x64-2 | 8 | 18 | 23 | 32 | 75/75 |
| ubicloud-x64-2 | 8 | 19 | 27 | 277 | 75/75 |
| **tensorlake-x64-2x8** | 8 | 19 | 21 | 87 | 15/15 |
| runson-i7i-large | 16 | 20 | 23 | 25 | 60/60 |
| runson-m8i-large | 8 | 20 | 52 | 278 | 60/60 |
| codebuild-x64-2x3 | 3 | 21 | 24 | 29 | 75/75 |
| runson-m8id-large | 8 | 21 | 24 | 25 | 60/60 |

### 4 vCPU

| Runner | RAM | Queue p50 | p90 | max | Jobs ok |
|---|---:|---:|---:|---:|---:|
| github-x64 | 16 | 4 | 6 | 42 | 75/75 |
| blacksmith-x64 | 16 | 11 | 14 | 15 | 75/75 |
| starsling-x64 | 16 | 11 | 12 | 13 | 75/75 |
| avrea-x64 | 16 | 12 | 88 | 93 | 75/75 |
| warpbuild-x64 | 16 | 13 | 14 | 16 | 75/75 |
| **tensorlake-x64** | 16 | 14 | 16 | 17 | 15/15 |
| namespace-x64 | 16 | 17 | 21 | 21 | 15/15 |
| runson-m8a-x64 | 16 | 17 | 21 | 82 | 60/60 |
| runson-m8i-flex-xlarge | 16 | 17 | 20 | 22 | 60/60 |
| runson-r8a-tmpfs-x64 | 32 | 18 | 22 | 29 | 60/60 |
| runson-m8azn-x64 | 16 | 18 | 44 | 52 | 60/60 |
| runson-m8i-xlarge | 16 | 18 | 25 | 1,319 | 60/60 |
| namespace-x64-4x8 | 8 | 19 | 24 | 27 | 15/15 |
| runson-c8a-x64-4x8 | 8 | 19 | 47 | 71 | 60/60 |
| runson-i7i-xlarge | 32 | 20 | 23 | 25 | 60/60 |
| runson-m8azn-gp3tuned-x64 | 16 | 20 | 49 | 57 | 60/60 |
| ubicloud-premium-x64 | 16 | 20 | 27 | 31 | 75/75 |
| codebuild-x64 | 8 | 21 | 81 | 85 | 75/75 |
| runson-m8id-x64 | 16 | 22 | 27 | 30 | 60/60 |
| ubicloud-x64 | 16 | 22 | 26 | 32 | 75/75 |

### 8 vCPU

| Runner | RAM | Queue p50 | p90 | max | Jobs ok |
|---|---:|---:|---:|---:|---:|
| blacksmith-x64-8x32 | 32 | 10 | 13 | 15 | 75/75 |
| warpbuild-x64-8x32 | 32 | 12 | 14 | 29 | 75/75 |
| starsling-x64-8x32 | 32 | 13 | 78 | 95 | 75/75 |
| avrea-x64-8x32 | 32 | 14 | 167 | 302 | 75/75 |
| namespace-x64-8x32 | 32 | 17 | 29 | 31 | 15/15 |
| runson-c8a-x64-8x16 | 16 | 17 | 22 | 37 | 60/60 |
| runson-m8a-2xlarge | 32 | 17 | 19 | 22 | 60/60 |
| ubicloud-premium-x64-8x32 | 32 | 17 | 23 | 26 | 75/75 |
| runson-m8i-flex-2xlarge | 32 | 18 | 20 | 23 | 60/60 |
| runson-m8a-2xlarge-gp3tuned | 32 | 18 | 21 | 30 | 60/60 |
| runson-m8a-2xlarge-tmpfs | 32 | 18 | 50 | 57 | 60/60 |
| runson-m8i-2xlarge | 32 | 18 | 24 | 34 | 60/60 |
| runson-m8id-2xlarge | 32 | 18 | 22 | 27 | 60/60 |
| namespace-x64-8x16 | 16 | 19 | 25 | 151 | 15/15 |
| runson-r8a-2xlarge-tmpfs-x64 | 64 | 19 | 50 | 56 | 60/60 |
| codebuild-x64-8x16 | 16 | 21 | 22 | 25 | 75/75 |
| ubicloud-x64-8x32 | 32 | 21 | 167 | 277 | 75/75 |
| **tensorlake-x64-8x32** | 32 | 21 | 89 | 90 | 15/15 |
| runson-i7i-2xlarge | 64 | 23 | 27 | 29 | 60/60 |
| github-x64-8x32 | 32 | 80 | 91 | 97 | 75/75 |

