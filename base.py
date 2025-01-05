import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os


class BaseClass:
    def __init__(self, url: str, headless: bool = False) -> None:
        load_dotenv()
        self.logger: logging.Logger = logging.getLogger(__name__)
        self.driver: WebDriver = self.setup_driver(headless)
        self.wait: WebDriverWait = WebDriverWait(self.driver, 20)
        self.url: str = url

    def setup_driver(self, headless: bool) -> WebDriver:
        try:
            self.logger.info("Setting up WebDriver")
            options: webdriver.FirefoxOptions = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
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

    def login(self) -> None:
        try:
            self.logger.info("Finding login link")
            button = self.wait.until(
                lambda d: d.find_element(
                    By.XPATH, "//div[@class='user-nav']/a[text()='LOGIN']"
                )
            )
            button.click()
            self.logger.info("Login link clicked")

            self.logger.info("Entering username")
            username_input = self.wait.until(
                lambda d: d.find_element(
                    By.CSS_SELECTOR,
                    'input[type="text"][name="username"][autocomplete="username"]',
                )
            )
            username_input.send_keys(os.getenv("USERNAME"))
            self.logger.info("Username entered")

            self.logger.info("Entering password")
            password_input = self.wait.until(
                lambda d: d.find_element(
                    By.CSS_SELECTOR,
                    'input[type="password"][name="password"][autocomplete="current-password"]',
                )
            )
            password_input.send_keys(os.getenv("PASSWORD"))
            self.logger.info("Password entered")

            self.logger.info("Submitting form")
            submit_button = self.wait.until(
                lambda d: d.find_element(
                    By.CSS_SELECTOR,
                    'input[type="submit"][class="css-z5gx6u e19owgy712"]',
                )
            )
            submit_button.click()
            self.logger.info("Form submitted")

            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Failed to login: {e}")

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

    def save_score(self) -> None:
        try:
            self.logger.info("Saving score")
            self.click_button("Save score")
            self.logger.info("Score saved")
        except Exception as e:
            self.logger.error(f"Failed to save score: {e}")

    def run(self) -> None:
        self.logger.info("Starting run method")
        try:
            # Navigate to the main page and login
            self.driver.get("https://humanbenchmark.com")
            self.login()

            # Navigate to the specific test URL
            self.driver.get(self.url)

            self.click_start()
            self.perform_test()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        finally:
            self.save_score()
            self.teardown_driver()
            self.logger.info("Run method complete")

    def click_start(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    def perform_test(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")
