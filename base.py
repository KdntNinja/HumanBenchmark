import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class BaseMemory:
    def __init__(self, url: str, headless: bool = True) -> None:
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

    def run(self) -> None:
        self.logger.info("Starting run method")
        try:
            self.driver.get(self.url)
            self.click_start()
            self.perform_test()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        finally:
            self.teardown_driver()
            self.logger.info("Run method complete")

    def click_start(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    def perform_test(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")
