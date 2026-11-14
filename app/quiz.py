import random

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": "Jupiter",
    },
    {
        "question": "What is the chemical formula for water?",
        "options": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O",
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": [
            "William Shakespeare",
            "Charles Dickens",
            "Mark Twain",
            "Jane Austen",
        ],
        "answer": "William Shakespeare",
    },
    {
        "question": "What is the speed of light?",
        "options": ["3 x 10^8 m/s", "1 x 10^6 m/s", "5 x 10^7 m/s", "2 x 10^9 m/s"],
        "answer": "3 x 10^8 m/s",
    },
]

QUIT_WORDS = {"q", "quit", "exit"}


class QuitQuiz(Exception):
    """Raised when the player wants to stop (typed 'q', Ctrl-C or Ctrl-D)."""


def validate_questions(questions):
    """Fail early if the question data is broken."""
    for item in questions:
        if item["answer"] not in item["options"]:
            raise ValueError(f"Answer not among the options: {item['question']!r}")
        if len(set(item["options"])) != len(item["options"]):
            raise ValueError(f"Duplicate options: {item['question']!r}")


# ===== NEW: used by the web routes in main.py (and by the terminal game) =====
def get_questions():
    """Return all questions, in random order."""
    validate_questions(QUESTIONS)
    return random.sample(QUESTIONS, k=len(QUESTIONS))


def shuffled_options(item):
    """Return the options of one question in random order."""
    return random.sample(item["options"], k=len(item["options"]))


def is_correct(item, choice):
    """Return True if the chosen option text is the right answer."""
    return choice == item["answer"]


# ===== END NEW =====
def read_input(prompt):
    try:
        text = input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        raise QuitQuiz
    if text.lower() in QUIT_WORDS:
        raise QuitQuiz
    return text


def ask_choice(num_options):
    """Ask until the player enters a valid option number; return a 0-based index."""
    while True:
        text = read_input(f"Your answer (1-{num_options}, or q to quit): ")
        try:
            choice = int(text)
        except ValueError:
            choice = None
        if choice is not None and 1 <= choice <= num_options:
            return choice - 1
        print(f"Invalid input. Enter a number from 1 to {num_options}.")


def ask_yes_no(prompt):

    while True:
        text = read_input(f"{prompt} (y/n): ").lower()
        if text in ("y", "yes"):
            return True
        if text in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def ask_question(item, number, total):
    """Show one question (options shuffled). Return True if answered correctly."""
    options = shuffled_options(
        item
    )  # CHANGED: was random.sample(item["options"], k=len(item["options"]))
    print(f"\nQuestion {number}/{total}: {item['question']}")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")

    picked = options[ask_choice(len(options))]
    if is_correct(item, picked):  # CHANGED: was  if picked == item["answer"]:
        print("Correct!")
        return True
    print(f"Wrong! The correct answer is: {item['answer']}")
    return False


def run_quiz():  # CHANGED: was  def run_quiz(questions):
    """Ask every question once in random order and print the score."""
    order = (
        get_questions()
    )  # CHANGED: was  order = random.sample(questions, k=len(questions))
    score = answered = 0
    try:
        for number, item in enumerate(order, start=1):
            if ask_question(item, number, len(order)):
                score += 1
            answered += 1
    finally:
        # Also shown if the player quits part-way through.
        print(f"\nScore: {score}/{answered}")


def main():
    validate_questions(QUESTIONS)
    print("Welcome to the Quiz! (type q at any time to quit)")
    try:
        while True:
            run_quiz()  # CHANGED: was  run_quiz(QUESTIONS)
            if not ask_yes_no("\nPlay again?"):
                break
    except QuitQuiz:
        pass
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
