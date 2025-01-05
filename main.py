import logging

import inquirer

from number_memory import NumberMemory
from reaction_speed import ReactionSpeed
from typing_speed import TypingSpeed
from verbal_memory import VerbalMemory

# --- Logging Setup ---
log_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("workflow_log.txt", mode="w")

console_handler.setFormatter(log_formatter)
file_handler.setFormatter(log_formatter)

logger = logging.getLogger("HumanBenchmark")
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def main():
    tests = {
        "Reaction Speed": ReactionSpeed,
        "Typing Speed": TypingSpeed,
        "Number Memory": NumberMemory,
        "Verbal Memory": VerbalMemory,
    }

    questions = [
        inquirer.List(
            "test",
            message="Which test would you like to run?",
            choices=list(tests.keys()),
        ),
        inquirer.Confirm(
            "headless",
            message="Would you like to run in headless mode?",
            default=False,
        ),
    ]
    answers = inquirer.prompt(questions)

    selected_test = tests[answers["test"]](headless=answers["headless"])
    selected_test.run()


if __name__ == "__main__":
    main()
