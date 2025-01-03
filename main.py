import inquirer
import logging
import sys

from number_memory import NumberMemory
from verbal_memory import VerbalMemory

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    questions = [
        inquirer.List(
            "test",
            message="Which test would you like to run?",
            choices=["Number Memory", "Verbal Memory"],
        ),
        inquirer.Confirm(
            "headless",
            message="Do you want to run the browser in headless mode?",
            default=True,
        ),
    ]
    answers = inquirer.prompt(questions)

    headless = answers["headless"]

    if answers["test"] == "Number Memory":
        number_memory_test = NumberMemory(headless=headless)
        number_memory_test.run()
    elif answers["test"] == "Verbal Memory":
        verbal_memory_test = VerbalMemory(headless=headless)
        verbal_memory_test.run()


if __name__ == "__main__":
    main()
