# Option Combinations Test Plan and Execution Report

## Scope
- Target script: `_ai_agent/.agents_management/opencode_starter/scripts/install.sh`
- Target makefile: `_ai_agent/.agents_management/opencode_starter/Makefile`
- Execution date: 2026-04-16T11:01:12.715651

## Enumerated Option Spaces
### install.sh CLI flags
- `--no-update`
- `--update`
- `--skip-make`
- `--dry-run`
- `--overwrite`
- `--uninstall`
- `--force`
- `--help` (explicit single-path validation)

Total combinations over primary flag space: **128** (`2^7`)

### Makefile targets and variable dimensions
- Make targets discovered via `##` help annotations: **19**
  - `help`
  - `check`
  - `dry-run`
  - `install-force`
  - `preflight-targets`
  - `install`
  - `install-ln`
  - `uninstall`
  - `uninstall-ln`
  - `restow`
  - `status`
  - `list`
  - `clean`
  - `install-all`
  - `uninstall-all`
  - `install-hooks`
  - `uninstall-hooks`
  - `run-hooks`
  - `update-hooks`
- Variable dimensions tested:
  - `DRY_RUN`: {0,1}
  - `FORCE_OVERWRITE`: {0,1}
- Target-variable combinations: **76**

## Test Plan
1. Run all 128 install.sh combinations in canonical flag order.
2. Safety guard: append `--dry-run` to any combination that does not include it.
3. Execute explicit `--help` path once.
4. For Makefile, run every `(target, DRY_RUN, FORCE_OVERWRITE)` tuple if a make binary exists.
5. Record PASS/FAIL/BLOCKED and sample output.

## Execution Summary
- install.sh: PASS=0, FAIL=128, TOTAL=128 (+help path status=FAIL)
- Makefile: PASS=0, FAIL=0, BLOCKED=76, TOTAL=76
- Make command used: **None found** (`make`, `mingw32-make`, `gmake` absent from PATH)

## install.sh Combination Results (Primary Space)
| idx | flags | effective flags | dry-run injected | status | exit | sample |
|---:|---|---|:---:|:---:|---:|---|
| 0 | `(none)` | `--dry-run` | true | FAIL | 1 | <3>WSL (74761 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 1 | `--no-update` | `--no-update --dry-run` | true | FAIL | 1 | <3>WSL (74764 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 2 | `--update` | `--update --dry-run` | true | FAIL | 1 | <3>WSL (74767 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 3 | `--no-update --update` | `--no-update --update --dry-run` | true | FAIL | 1 | <3>WSL (74770 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 4 | `--skip-make` | `--skip-make --dry-run` | true | FAIL | 1 | <3>WSL (74773 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 5 | `--no-update --skip-make` | `--no-update --skip-make --dry-run` | true | FAIL | 1 | <3>WSL (74776 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 6 | `--update --skip-make` | `--update --skip-make --dry-run` | true | FAIL | 1 | <3>WSL (74779 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 7 | `--no-update --update --skip-make` | `--no-update --update --skip-make --dry-run` | true | FAIL | 1 | <3>WSL (74782 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 8 | `--dry-run` | `--dry-run` | false | FAIL | 1 | <3>WSL (74785 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 9 | `--no-update --dry-run` | `--no-update --dry-run` | false | FAIL | 1 | <3>WSL (74806 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 10 | `--update --dry-run` | `--update --dry-run` | false | FAIL | 1 | <3>WSL (74809 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 11 | `--no-update --update --dry-run` | `--no-update --update --dry-run` | false | FAIL | 1 | <3>WSL (74812 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 12 | `--skip-make --dry-run` | `--skip-make --dry-run` | false | FAIL | 1 | <3>WSL (74815 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 13 | `--no-update --skip-make --dry-run` | `--no-update --skip-make --dry-run` | false | FAIL | 1 | <3>WSL (74818 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 14 | `--update --skip-make --dry-run` | `--update --skip-make --dry-run` | false | FAIL | 1 | <3>WSL (74821 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 15 | `--no-update --update --skip-make --dry-run` | `--no-update --update --skip-make --dry-run` | false | FAIL | 1 | <3>WSL (74824 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 16 | `--overwrite` | `--overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74827 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 17 | `--no-update --overwrite` | `--no-update --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74830 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 18 | `--update --overwrite` | `--update --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74833 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 19 | `--no-update --update --overwrite` | `--no-update --update --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74836 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 20 | `--skip-make --overwrite` | `--skip-make --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74839 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 21 | `--no-update --skip-make --overwrite` | `--no-update --skip-make --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74842 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 22 | `--update --skip-make --overwrite` | `--update --skip-make --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74845 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 23 | `--no-update --update --skip-make --overwrite` | `--no-update --update --skip-make --overwrite --dry-run` | true | FAIL | 1 | <3>WSL (74848 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 24 | `--dry-run --overwrite` | `--dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74851 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 25 | `--no-update --dry-run --overwrite` | `--no-update --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74854 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 26 | `--update --dry-run --overwrite` | `--update --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74857 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 27 | `--no-update --update --dry-run --overwrite` | `--no-update --update --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74860 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 28 | `--skip-make --dry-run --overwrite` | `--skip-make --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74863 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 29 | `--no-update --skip-make --dry-run --overwrite` | `--no-update --skip-make --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74866 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 30 | `--update --skip-make --dry-run --overwrite` | `--update --skip-make --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74869 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 31 | `--no-update --update --skip-make --dry-run --overwrite` | `--no-update --update --skip-make --dry-run --overwrite` | false | FAIL | 1 | <3>WSL (74872 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 32 | `--uninstall` | `--uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74875 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 33 | `--no-update --uninstall` | `--no-update --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74878 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 34 | `--update --uninstall` | `--update --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74881 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 35 | `--no-update --update --uninstall` | `--no-update --update --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74884 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 36 | `--skip-make --uninstall` | `--skip-make --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74887 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 37 | `--no-update --skip-make --uninstall` | `--no-update --skip-make --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74890 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 38 | `--update --skip-make --uninstall` | `--update --skip-make --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74893 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 39 | `--no-update --update --skip-make --uninstall` | `--no-update --update --skip-make --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74896 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 40 | `--dry-run --uninstall` | `--dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74899 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 41 | `--no-update --dry-run --uninstall` | `--no-update --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74902 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 42 | `--update --dry-run --uninstall` | `--update --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74905 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 43 | `--no-update --update --dry-run --uninstall` | `--no-update --update --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74908 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 44 | `--skip-make --dry-run --uninstall` | `--skip-make --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74911 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 45 | `--no-update --skip-make --dry-run --uninstall` | `--no-update --skip-make --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74914 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 46 | `--update --skip-make --dry-run --uninstall` | `--update --skip-make --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74917 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 47 | `--no-update --update --skip-make --dry-run --uninstall` | `--no-update --update --skip-make --dry-run --uninstall` | false | FAIL | 1 | <3>WSL (74920 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 48 | `--overwrite --uninstall` | `--overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74923 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 49 | `--no-update --overwrite --uninstall` | `--no-update --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74926 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 50 | `--update --overwrite --uninstall` | `--update --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74929 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 51 | `--no-update --update --overwrite --uninstall` | `--no-update --update --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74932 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 52 | `--skip-make --overwrite --uninstall` | `--skip-make --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74935 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 53 | `--no-update --skip-make --overwrite --uninstall` | `--no-update --skip-make --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74938 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 54 | `--update --skip-make --overwrite --uninstall` | `--update --skip-make --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74960 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 55 | `--no-update --update --skip-make --overwrite --uninstall` | `--no-update --update --skip-make --overwrite --uninstall --dry-run` | true | FAIL | 1 | <3>WSL (74963 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 56 | `--dry-run --overwrite --uninstall` | `--dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74966 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 57 | `--no-update --dry-run --overwrite --uninstall` | `--no-update --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74969 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 58 | `--update --dry-run --overwrite --uninstall` | `--update --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74972 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 59 | `--no-update --update --dry-run --overwrite --uninstall` | `--no-update --update --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74975 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 60 | `--skip-make --dry-run --overwrite --uninstall` | `--skip-make --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74978 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 61 | `--no-update --skip-make --dry-run --overwrite --uninstall` | `--no-update --skip-make --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74981 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 62 | `--update --skip-make --dry-run --overwrite --uninstall` | `--update --skip-make --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74984 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 63 | `--no-update --update --skip-make --dry-run --overwrite --uninstall` | `--no-update --update --skip-make --dry-run --overwrite --uninstall` | false | FAIL | 1 | <3>WSL (74987 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 64 | `--force` | `--force --dry-run` | true | FAIL | 1 | <3>WSL (74990 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 65 | `--no-update --force` | `--no-update --force --dry-run` | true | FAIL | 1 | <3>WSL (74993 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 66 | `--update --force` | `--update --force --dry-run` | true | FAIL | 1 | <3>WSL (74996 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 67 | `--no-update --update --force` | `--no-update --update --force --dry-run` | true | FAIL | 1 | <3>WSL (74999 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 68 | `--skip-make --force` | `--skip-make --force --dry-run` | true | FAIL | 1 | <3>WSL (75002 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 69 | `--no-update --skip-make --force` | `--no-update --skip-make --force --dry-run` | true | FAIL | 1 | <3>WSL (75005 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 70 | `--update --skip-make --force` | `--update --skip-make --force --dry-run` | true | FAIL | 1 | <3>WSL (75008 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 71 | `--no-update --update --skip-make --force` | `--no-update --update --skip-make --force --dry-run` | true | FAIL | 1 | <3>WSL (75011 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 72 | `--dry-run --force` | `--dry-run --force` | false | FAIL | 1 | <3>WSL (75014 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 73 | `--no-update --dry-run --force` | `--no-update --dry-run --force` | false | FAIL | 1 | <3>WSL (75017 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 74 | `--update --dry-run --force` | `--update --dry-run --force` | false | FAIL | 1 | <3>WSL (75020 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 75 | `--no-update --update --dry-run --force` | `--no-update --update --dry-run --force` | false | FAIL | 1 | <3>WSL (75023 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 76 | `--skip-make --dry-run --force` | `--skip-make --dry-run --force` | false | FAIL | 1 | <3>WSL (75026 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 77 | `--no-update --skip-make --dry-run --force` | `--no-update --skip-make --dry-run --force` | false | FAIL | 1 | <3>WSL (75029 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 78 | `--update --skip-make --dry-run --force` | `--update --skip-make --dry-run --force` | false | FAIL | 1 | <3>WSL (75032 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 79 | `--no-update --update --skip-make --dry-run --force` | `--no-update --update --skip-make --dry-run --force` | false | FAIL | 1 | <3>WSL (75035 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 80 | `--overwrite --force` | `--overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75038 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 81 | `--no-update --overwrite --force` | `--no-update --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75041 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 82 | `--update --overwrite --force` | `--update --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75044 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 83 | `--no-update --update --overwrite --force` | `--no-update --update --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75047 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 84 | `--skip-make --overwrite --force` | `--skip-make --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75050 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 85 | `--no-update --skip-make --overwrite --force` | `--no-update --skip-make --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75053 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 86 | `--update --skip-make --overwrite --force` | `--update --skip-make --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75056 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 87 | `--no-update --update --skip-make --overwrite --force` | `--no-update --update --skip-make --overwrite --force --dry-run` | true | FAIL | 1 | <3>WSL (75059 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 88 | `--dry-run --overwrite --force` | `--dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75062 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 89 | `--no-update --dry-run --overwrite --force` | `--no-update --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75065 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 90 | `--update --dry-run --overwrite --force` | `--update --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75068 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 91 | `--no-update --update --dry-run --overwrite --force` | `--no-update --update --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75071 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 92 | `--skip-make --dry-run --overwrite --force` | `--skip-make --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75074 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 93 | `--no-update --skip-make --dry-run --overwrite --force` | `--no-update --skip-make --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75077 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 94 | `--update --skip-make --dry-run --overwrite --force` | `--update --skip-make --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75080 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 95 | `--no-update --update --skip-make --dry-run --overwrite --force` | `--no-update --update --skip-make --dry-run --overwrite --force` | false | FAIL | 1 | <3>WSL (75083 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 96 | `--uninstall --force` | `--uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75086 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 97 | `--no-update --uninstall --force` | `--no-update --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75089 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 98 | `--update --uninstall --force` | `--update --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75092 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 99 | `--no-update --update --uninstall --force` | `--no-update --update --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75095 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 100 | `--skip-make --uninstall --force` | `--skip-make --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75098 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 101 | `--no-update --skip-make --uninstall --force` | `--no-update --skip-make --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75101 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 102 | `--update --skip-make --uninstall --force` | `--update --skip-make --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75104 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 103 | `--no-update --update --skip-make --uninstall --force` | `--no-update --update --skip-make --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75107 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 104 | `--dry-run --uninstall --force` | `--dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75110 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 105 | `--no-update --dry-run --uninstall --force` | `--no-update --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75113 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 106 | `--update --dry-run --uninstall --force` | `--update --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75116 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 107 | `--no-update --update --dry-run --uninstall --force` | `--no-update --update --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75119 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 108 | `--skip-make --dry-run --uninstall --force` | `--skip-make --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75122 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 109 | `--no-update --skip-make --dry-run --uninstall --force` | `--no-update --skip-make --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75125 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 110 | `--update --skip-make --dry-run --uninstall --force` | `--update --skip-make --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75128 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 111 | `--no-update --update --skip-make --dry-run --uninstall --force` | `--no-update --update --skip-make --dry-run --uninstall --force` | false | FAIL | 1 | <3>WSL (75131 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 112 | `--overwrite --uninstall --force` | `--overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75134 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 113 | `--no-update --overwrite --uninstall --force` | `--no-update --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75137 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 114 | `--update --overwrite --uninstall --force` | `--update --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75140 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 115 | `--no-update --update --overwrite --uninstall --force` | `--no-update --update --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75143 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 116 | `--skip-make --overwrite --uninstall --force` | `--skip-make --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75146 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 117 | `--no-update --skip-make --overwrite --uninstall --force` | `--no-update --skip-make --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75149 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 118 | `--update --skip-make --overwrite --uninstall --force` | `--update --skip-make --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75152 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 119 | `--no-update --update --skip-make --overwrite --uninstall --force` | `--no-update --update --skip-make --overwrite --uninstall --force --dry-run` | true | FAIL | 1 | <3>WSL (75155 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 120 | `--dry-run --overwrite --uninstall --force` | `--dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75158 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 121 | `--no-update --dry-run --overwrite --uninstall --force` | `--no-update --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75161 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 122 | `--update --dry-run --overwrite --uninstall --force` | `--update --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75164 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 123 | `--no-update --update --dry-run --overwrite --uninstall --force` | `--no-update --update --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75167 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 124 | `--skip-make --dry-run --overwrite --uninstall --force` | `--skip-make --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75170 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 125 | `--no-update --skip-make --dry-run --overwrite --uninstall --force` | `--no-update --skip-make --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75173 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 126 | `--update --skip-make --dry-run --overwrite --uninstall --force` | `--update --skip-make --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75176 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |
| 127 | `--no-update --update --skip-make --dry-run --overwrite --uninstall --force` | `--no-update --update --skip-make --dry-run --overwrite --uninstall --force` | false | FAIL | 1 | <3>WSL (75179 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory |

### install.sh explicit help result
| flags | status | exit | sample |
|---|:---:|---:|---|
| `--help` | FAIL | 1 |  |

## Makefile Target/Variable Matrix Results
| target | DRY_RUN | FORCE_OVERWRITE | status | exit | note/sample |
|---|---:|---:|:---:|---:|---|
| `help` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `help` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `help` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `help` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `check` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `check` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `check` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `check` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `dry-run` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `dry-run` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `dry-run` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `dry-run` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-force` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-force` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-force` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-force` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `preflight-targets` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `preflight-targets` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `preflight-targets` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `preflight-targets` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-ln` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-ln` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-ln` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-ln` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-ln` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-ln` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-ln` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-ln` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `restow` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `restow` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `restow` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `restow` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `status` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `status` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `status` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `status` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `list` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `list` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `list` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `list` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `clean` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `clean` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `clean` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `clean` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-all` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-all` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-all` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-all` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-all` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-all` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-all` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-all` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-hooks` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-hooks` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-hooks` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `install-hooks` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-hooks` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-hooks` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-hooks` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `uninstall-hooks` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `run-hooks` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `run-hooks` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `run-hooks` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `run-hooks` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `update-hooks` | 0 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `update-hooks` | 0 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `update-hooks` | 1 | 0 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
| `update-hooks` | 1 | 1 | BLOCKED |  | No make-compatible binary found in PATH (make/mingw32-make/gmake). |
