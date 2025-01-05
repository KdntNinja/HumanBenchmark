from selenium.webdriver.common.by import By

from base import BaseClass


class NumberMemory(BaseClass):
    def __init__(self, headless: bool = False) -> None:
        super().__init__("https://humanbenchmark.com/tests/number-memory", headless)
        self.number: str = ""
        self.StartButton: str = "Start"
        self.SubmitButton: str = "Submit"
        self.NextButton: str = "NEXT"

    def click_start(self) -> None:
        self.click_button(self.StartButton)

    def perform_test(self) -> None:
        while True:
            try:
                self.read_number()
                self.input_number()
                self.click_submit()
                self.click_next()
            except Exception as e:
                self.logger.error(f"Failed to perform test: {e}")
                break

    def read_number(self) -> None:
        try:
            self.logger.info("Reading number from the page")
            number_div = self.wait.until(
                lambda d: d.find_element(By.CSS_SELECTOR, "div.big-number")
            )
            self.number = number_div.text.strip()
            self.logger.info(f"Number read: {self.number}")
        except Exception as e:
            self.logger.error(f"Failed to read number: {e}")

    def input_number(self) -> None:
        try:
            self.logger.info(f"Inputting number: {self.number}")
            input_box = None
            while not input_box:
                input_box = self.wait.until(
                    lambda d: d.find_element(
                        By.CSS_SELECTOR, 'input[type="text"][pattern="[0-9]*"]'
                    ),
                    message="Input box not found",
                )
            input_box.send_keys(self.number)
            self.logger.info(f"Number inputted: {self.number}")
        except Exception as e:
            self.logger.error(f"Failed to input number: {e}")

    def click_submit(self) -> None:
        self.click_button(self.SubmitButton)

    def click_next(self) -> None:
        self.click_button(self.NextButton)
