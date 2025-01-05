import questionary
import logging
import sys
from questionary import Style

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

custom_style = Style(
    [
        ("qmark", "fg:#E91E63 bold"),  # Question mark
        ("question", "fg:#673AB7 bold"),  # Question text
        ("answer", "fg:#2196F3 bold"),  # Answer text
        ("pointer", "fg:#FF5722 bold"),  # Pointer for list options
        ("highlighted", "fg:#FFEB3B bold"),  # Highlighted option
        ("selected", "fg:#4CAF50 bold"),  # Selected option
        ("separator", "fg:#BDBDBD"),  # Separator line
        ("instruction", "fg:#9E9E9E"),  # User instructions
        ("text", "fg:#FFFFFF"),  # Plain text
        ("disabled", "fg:#757575 italic"),  # Disabled options
    ]
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
        {
            "type": "list",
            "name": "test",
            "message": "Which test would you like to run?",
            "choices": list(tests.keys()),
        },
        {
            "type": "confirm",
            "name": "headless",
            "message": "Run in headless mode (not recommended)?",
            "default": False,
        },
    ]
    answers = questionary.prompt(questions, style=custom_style)
    if not answers:
        print("No valid input provided. Exiting.")
        sys.exit(1)

    selected_test = tests[answers["test"]](headless=answers["headless"])
    selected_test.run()


if __name__ == "__main__":
    main()
