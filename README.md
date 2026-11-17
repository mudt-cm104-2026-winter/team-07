# Team project

<!-- Replace the title with your project name. -->

## What this is

<!-- One or two sentences: what does your app do, and who is it for?
Right now it is the example "Things to bring". Replace it with your topic. -->

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.

## Team

<!-- One row per person: GitHub username and what you mainly take care of.
No real names: this repository is public. -->

| GitHub | Role |
|Ventspils|gamer|
|Pierrmon|Italian|
|---|---|

## How we work

<!-- How your team uses Git. For example:
- one branch per issue, named after it: `12-add-glossary`
- every pull request needs one approval from another team member
- the author merges after the approval
- every pull request adds a line to CHANGELOG.md
-->

## Sources
<<<<<<< HEAD
- 2026-11-10: Python documentation, used for understanding how routing between web pages works
- 2026-11-10: Google search on how FastAPI handles forms, used for understanding how the buttons send data to the routes

## Use of AI
- 2026-11-10: Claude, used for explaining and planning the routes in main.py, checked by testing every route in /docs
- 2026-11-13: Claude, used for suggesting changes to quiz.py so main.py can use it, checked by running the terminal game and the web routes
- 2026-11-15: Claude, used for the HTML templates and CSS, checked by playing full games in the browser (desktop and mobile view)
=======

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->
- 2026-11-13: https://stackoverflow.com/questions/76406799/making-a-json-saving-system-for-my-python-game, used as a referance for storage.py

## Use of AI

<!-- One entry per use, added on the day you use it:
- 2026-11-05: <tool>, used for <what>, checked by <how you checked the result>
"none" is a valid entry.
-->
- 2026-11-13: Gemini, used for modifications of the storage.py code, the result was reviewed by Ventspils and later tested succesfully
- 2026-11-13: Claude, used for modification of the quiz.py code, checked by Pierrmon by review and testing in the terminal
- 2026-11-13: Claude, used for constricting the skeleton structure of the routing, reiewed by TownMax
>>>>>>> origin/main
