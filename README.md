# Quiz Game 



## What this is

A multiple-choice quiz built with Python and FastAPI. Players answer a series of shuffled questions in the browser, get instant feedback after each answer, and see their final score next to the all-time highscore, which is saved to disk.

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The `json` module reads and writes the highscore in `data.json`. Because the file is on disk, the highscore survives a restart, while games in progress (kept in memory) are lost.

## Team

<!-- One row per person: GitHub username and what you mainly take care of.
No real names: this repository is public. -->

| GitHub | Mainly takes care of |
|---|---|
| TownMax | `main.py`: web routes and game state |
| Pierrmon | `quiz.py`: questions, shuffling and answer checking |
| Ventspils | `storage.py`:                    |
|---|---|

## How we work

<!-- How your team uses Git. For example:
- one branch per issue, named after it: `12-add-glossary`
- every pull request needs one approval from another team member
- the author merges after the approval
- every pull request adds a line to CHANGELOG.md
-->
How the team worked:


- created and assigned issues to each member before starting the project
- one branch per issue, named after it
- while working on an issue, the issue was moved from "Todo" to "In Progress" by the member working on it
- when an issue was solved, it was then closed and moved to the "Done" column on the board.
- after solving an issue, the respective branch was deleted 
- Main branch was protected, nobody could push to it directly.
- every pull request needs one approval from another team member
- the author merges after the approval



## Sources

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI

<!-- One entry per use, added on the day you use it:
- 2026-11-05: <tool>, used for <what>, checked by <how you checked the result>
"none" is a valid entry.
-->
