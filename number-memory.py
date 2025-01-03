import logging
import os
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class HumanBenchmark:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)
        self.driver: WebDriver = self.setup_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, 20)
        self.url: str = "https://humanbenchmark.com/tests/number-memory"
        self.number: str = ""

        # Buttons
        self.StartButton: str = "Start"
        self.SubmitButton: str = "Submit"
        self.NextButton: str = "NEXT"

    def setup_driver(self) -> WebDriver:
        try:
            self.logger.info("Setting up WebDriver")
            options: webdriver.FirefoxOptions = webdriver.FirefoxOptions()
            # options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            self.logger.info("WebDriver setup complete")
            return driver
        except Exception as e:
            self.logger.error(f"Failed to set up WebDriver: {e}")
            raise

    def teardown_driver(self) -> None:
        self.logger.info("Tearing down WebDriver")
        if self.driver:
            self.driver.quit()
        self.logger.info("WebDriver teardown complete")
        os.system("pkill geckodriver")

    def click_button(self, element: str) -> None:
        try:
            self.logger.info(f"Clicking button: {element}")
            button = self.wait.until(
                lambda d: d.find_element(By.XPATH, f"//button[text()='{element}']")
            )
            button.click()
            self.logger.info(f"Button clicked: {element}")
        except Exception as e:
            self.logger.error(f"Failed to click button: {e}")

    def click_start(self) -> None:
        self.click_button(self.StartButton)

    def click_submit(self) -> None:
        self.click_button(self.SubmitButton)

    def click_next(self) -> None:
        self.click_button(self.NextButton)

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
            input_box = self.wait.until(
                lambda d: d.find_element(
                    By.CSS_SELECTOR, 'input[type="text"][pattern="[0-9]*"]'
                )
            )
            if input_box:
                input_box.send_keys(self.number)
                self.logger.info(f"Number inputted: {self.number}")
            else:
                self.logger.error("Input box not found")
        except Exception as e:
            self.logger.error(f"Failed to input number: {e}")

    def run(self) -> None:
        self.logger.info("Starting run method")
        try:
            self.driver.get(self.url)
            self.click_start()
            while True:
                self.read_number()
                self.input_number()
                self.click_submit()
                self.click_next()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        finally:
            self.teardown_driver()
            self.logger.info("Run method complete")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    solver: HumanBenchmark = HumanBenchmark()

    def run_solver() -> None:
        solver.run()

    t: threading.Thread = threading.Thread(target=run_solver)
    t.start()
    t.join()
