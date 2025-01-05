import inquirer
import logging
import sys

from typing_speed import TypingSpeed
from reaction_speed import ReactionSpeed
from number_memory import NumberMemory
from verbal_memory import VerbalMemory
from chimp_test import ChimpTest

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def main():
    tests = {
        "Chimp Test": ChimpTest,
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
