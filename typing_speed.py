from selenium.webdriver.common.by import By

from base import BaseClass


class TypingSpeed(BaseClass):
    def __init__(self) -> None:
        super().__init__("https://humanbenchmark.com/tests/typing")
        self.LettersDiv: str = "div.letters.notranslate"

    def click_start(self) -> None:
        pass

    def run(self) -> None:
        try:
            self.logger.info("Starting typing test")
            letters_div = self.wait.until(
                lambda d: d.find_element(By.CSS_SELECTOR, self.LettersDiv)
            )
            letters = letters_div.find_elements(By.TAG_NAME, "span")
            text_to_type = "".join(
                [letter.get_attribute("innerText") for letter in letters]
            )
            self.logger.info(f"Text to type: {text_to_type}")

            for char in text_to_type:
                self.driver.find_element(By.TAG_NAME, "body").send_keys(char)
            self.logger.info("Typing test completed")
        except Exception as e:
            self.logger.error(f"An error occurred during the typing test: {e}")
