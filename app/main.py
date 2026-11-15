"""Quiz Game: web routes for a multiple-choice quiz with a persistent highscore.

Module overview:
- main.py      HTTP routes and game state
- quiz.py      question data, shuffling and answer checking (<github-username>)
- storage.py   highscore persistence in data.json (<github-username>)
- templates/   HTML templates
- static/      stylesheet
"""

import uuid
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import quiz, storage

HERE = Path(__file__).parent

app = FastAPI(title="Quiz Game")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


# --- Game state -------------------------------------------------------

# Active games, keyed by game ID. Kept in memory, so running games are
# lost on restart. The highscore is persisted separately by storage.py.
games = {}


def find_game(game_id):
    # Return the game for the given ID or respond with 404 if it does not exist.
    game = games.get(game_id)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


def current_question(game):
    """Return the question the player is currently on."""
    return game["questions"][game["index"]]


# --- Routes -----------------------------------------------------------


@app.get("/")
def home():
    # Start page.
    # TODO (front end): render index.html
    return {"page": "start", "highscore": storage.get_high_score()}


@app.post("/start")
def start_game():
    # Create a new game with shuffled questions and redirect to the first question.
    questions = quiz.get_questions()
    game_id = uuid.uuid4().hex
    games[game_id] = {
        "questions": questions,
        "options": quiz.shuffled_options(questions[0]),
        "index": 0,
        "score": 0,
        "feedback": None,  # None until the current question is answered
        "finished": False,
    }
    return RedirectResponse(f"/game/{game_id}", status_code=303)


@app.get("/game/{game_id}")
def show_question(game_id: str):
    # Show the current question, including feedback once it has been answered.
    game = find_game(game_id)
    if game["finished"]:
        return RedirectResponse(f"/game/{game_id}/result", status_code=303)

    question = current_question(game)
    # TODO (front end): render question.html
    return {
        "game_id": game_id,
        "number": game["index"] + 1,
        "total": len(game["questions"]),
        "question": question["question"],
        "options": game["options"],
        "feedback": game["feedback"],
        "score": game["score"],
    }


@app.post("/game/{game_id}/answer")
def answer(game_id: str, choice: str = Form(...)):
    # Check the selected option and store the result.
    # Only the first answer per question is counted.

    game = find_game(game_id)

    if game["feedback"] is None and not game["finished"]:
        question = current_question(game)
        correct = quiz.is_correct(question, choice)
        if correct:
            game["score"] += 1
        game["feedback"] = {
            "choice": choice,
            "correct": correct,
            "right_answer": question["answer"],
        }

    return RedirectResponse(f"/game/{game_id}", status_code=303)


@app.post("/game/{game_id}/next")
def next_question(game_id: str):
    # Advance to the next question, or finish the game and save the score.
    game = find_game(game_id)

    # Ignore the request if the question is unanswered or the game is already over.
    if game["feedback"] is None or game["finished"]:
        return RedirectResponse(f"/game/{game_id}", status_code=303)

    game["index"] += 1
    game["feedback"] = None

    if game["index"] >= len(game["questions"]):
        game["finished"] = True
        storage.save_score(game["score"])
        return RedirectResponse(f"/game/{game_id}/result", status_code=303)

    # Shuffle once per question so the option order stays stable on reload.
    game["options"] = quiz.shuffled_options(current_question(game))
    return RedirectResponse(f"/game/{game_id}", status_code=303)


@app.get("/game/{game_id}/result")
def result(game_id: str):
    # Show the final score and the current highscore.
    game = find_game(game_id)
    # TODO (front end): render result.html
    return {
        "score": game["score"],
        "total": len(game["questions"]),
        "highscore": storage.get_high_score(),
    }
