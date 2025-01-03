from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import BaseClass


class ClickSpeed(BaseClass):
    def __init__(self) -> None:
        super().__init__("https://humanbenchmark.com/tests/reactiontime")
        self.BoxDiv: str = "div.css-42wpoy.e19owgy79"

    def click_start(self) -> None:
        box_div = self.wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, self.BoxDiv)
        )
        box_div.click()

    def click_box(self):
        box_div = self.wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, self.BoxDiv)
        )
        self.logger.info("Waiting for the box to turn green or text to change to 'Click!'")
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, f"{self.BoxDiv} div div h1 div"), "Click!")
        )
        box_div.click()
        self.logger.info("Clicked inside the box")

    def perform_test(self) -> None:
        try:
            self.logger.info("Starting click speed test")
            while True:
                self.click_box()
        except Exception as e:
            self.logger.error(f"An error occurred during the click speed test: {e}")
