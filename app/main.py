"""Quiz Game: a multiple-choice quiz with shuffled questions and a highscore.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- quiz.py      the quiz logic (<github-username>)
- storage.py   the highscore (<github-username>)
- templates/   the HTML pages
- static/      the stylesheet
"""

import random
import uuid
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# CHANGE LATER: when quiz.py and storage.py are ready, add:
# from . import quiz, storage

HERE = Path(__file__).parent

app = FastAPI(title="Quiz Game")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


# ===================================================================
# GAME STATE
# ===================================================================
games = {}  # ticket number (game_id) -> that game's info


def find_game(game_id):
    """Look up a game by its ticket number, or show 'not found'."""
    game = games.get(game_id)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


# ===================================================================
# ROUTES
# ===================================================================
@app.get("/")
def home():
    """Start page with a Start button."""
    # FRONT END LATER: show index.html
    pass


@app.post("/start")
def start_game():
    """Start button pressed: create a new game."""
    # 1. get the questions                          <- quiz.py
    # 2. shuffle the order with random.shuffle      <- or quiz.py, team decides
    # 3. make a ticket number with uuid.uuid4().hex
    # 4. put the new game on the board (games dict): order, index, score, feedback
    # 5. redirect to /game/{game_id}
    pass


@app.get("/game/{game_id}")
def show_question(game_id: str):
    """Show the current question, plus correct/wrong after a tap."""
    # 1. find the game with find_game()
    # 2. if the game is finished -> redirect to the result page
    # 3. get the current question                   <- quiz.py
    # FRONT END LATER: show question.html
    pass


@app.post("/game/{game_id}/answer")
def answer(game_id: str, choice: str = Form(...)):
    """An option button was tapped."""
    # 1. find the game
    # 2. only if not answered yet: check the choice  <- quiz.py
    # 3. if correct: add 1 to the score
    # 4. remember the feedback (correct or wrong)
    # 5. redirect back to the question page
    pass


@app.post("/game/{game_id}/next")
def next_question(game_id: str):
    """Next button pressed."""
    # 1. find the game
    # 2. move to the next question, clear the feedback
    # 3. if no questions are left: save the score    <- storage.py
    #    and redirect to the result page
    # 4. otherwise redirect to the question page
    pass


@app.get("/game/{game_id}/result")
def result(game_id: str):
    """Final score and the highscore."""
    # 1. find the game
    # 2. get the highscore                           <- storage.py
    # FRONT END LATER: show result.html
    pass
