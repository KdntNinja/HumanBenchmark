from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import BaseClass


class ClickSpeed(BaseClass):
    def __init__(self, headless: bool = False) -> None:
        super().__init__("https://humanbenchmark.com/tests/reactiontime", headless)
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
        self.logger.info("Waiting for text to change to 'Click!'")
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, f"{self.BoxDiv} div div h1 div"), "Click!"
            )
        )
        box_div.click()
        self.logger.info("Clicked inside the box")

        self.click_to_keep_going()

    def click_to_keep_going(self):
        h2_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//h2[text()='Click to keep going']"))
        )
        h2_element.click()

    def perform_test(self) -> None:
        try:
            self.logger.info("Starting click speed test")
            while True:
                self.click_box()
        except Exception as e:
            self.logger.error(f"An error occurred during the click speed test: {e}")
