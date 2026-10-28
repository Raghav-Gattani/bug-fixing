# 🐞 Bug Fixing Using Cursor AI

A program that averages a crew's bounties had two bugs. Cursor AI helped find and fix them.

| Bug | Problem | Fix |
|-----|---------|-----|
| 1 | `range(1, len(...))` skipped the first bounty, giving a wrong total | Loop directly over the list (`for bounty in bounties`) |
| 2 | Empty list caused `ZeroDivisionError` | Return `0` when the list is empty |

Files: `buggy_code.py` (before) and `fixed_code.py` (after).

**Author:** Raghav Gattani
