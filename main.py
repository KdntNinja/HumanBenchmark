import inquirer
import logging
import sys

from typing_speed import TypingSpeed
from click_speed import ClickSpeed
from number_memory import NumberClass
from verbal_memory import VerbalClass

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def main():
    tests = {
        "Click Speed": ClickSpeed,
        "Typing Speed": TypingSpeed,
        "Number Memory": NumberClass,
        "Verbal Memory": VerbalClass,
    }

    questions = [
        inquirer.List(
            "test",
            message="Which test would you like to run?",
            choices=list(tests.keys()),
        ),
    ]
    answers = inquirer.prompt(questions)

    selected_test = tests[answers["test"]]()
    selected_test.run()


if __name__ == "__main__":
    main()
