# Architecture Decision Record

| # | Decision | Alternatives | Reason |
|---|----------|--------------|--------|
| 1 | Terminal-only CLI, no GUI framework | Tkinter, web, curses | Staying true to the original single-file script's spirit. Zero dependencies beyond Python. |
| 2 | Dataclass for `Game` state | Dict, mutable class, global scope | Testability, immutability guardrails, and clear state boundaries. |
| 3 | `match/case` for guess results | if/elif chain, enum dispatch | Python 3.10+ pattern matching is self-documenting and the compiler checks exhaustiveness. |
| 4 | Separated display module | Inline ANSI in main.py | Keeps game logic pure. Swap `display.py` to add curses, web, or GUI without touching game code. |
| 5 | Category word lists in code | JSON file, API, DB | YAGNI — 50 words fit in <40 lines. File I/O adds complexity for zero benefit at this scale. |
| 6 | Public entry point (`word-guessing`) | `python -m` only | Giving both options means users can run without install or install for system-wide access. |
