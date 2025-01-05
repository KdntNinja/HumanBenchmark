from selenium.webdriver.common.by import By
from base import BaseClass


class VerbalMemory(BaseClass):
    def __init__(self, headless: bool = False) -> None:
        super().__init__("https://humanbenchmark.com/tests/verbal-memory", headless)
        self.word: str = ""
        self.seen_words: set = set()
        self.StartButton: str = "Start"
        self.SeenButton: str = "SEEN"
        self.NewButton: str = "NEW"

    def click_start(self) -> None:
        self.click_button(self.StartButton)

    def perform_test(self) -> None:
        while True:
            self.read_word()
            if self.word in self.seen_words:
                self.click_seen()
            else:
                self.seen_words.add(self.word)
                self.click_new()

    def read_word(self) -> None:
        try:
            self.logger.info("Reading word from the page")
            word_div = self.wait.until(
                lambda d: d.find_element(By.CSS_SELECTOR, "div.word")
            )
            self.word = word_div.text.strip()
            self.logger.info(f"Word read: {self.word}")
        except Exception as e:
            self.logger.error(f"Failed to read word: {e}")

    def click_seen(self) -> None:
        self.click_button(self.SeenButton)

    def click_new(self) -> None:
        self.click_button(self.NewButton)
