from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base import BaseClass


class ChimpTest(BaseClass):
    def __init__(self, headless: bool = False) -> None:
        super().__init__("https://humanbenchmark.com/tests/chimp", headless)

    def click_start(self) -> None:
        self.click_button("Start Test")

    def click_continue_button(self) -> None:
        self.click_button("Continue")

    def process_cells(self) -> None:
        self.logger.debug("Locating the parent div")
        parent_div = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.css-gmuwbf"))
        )

        self.logger.debug("Finding all child divs with the data-cellnumber attribute")
        cell_divs = parent_div.find_elements(By.CSS_SELECTOR, "div[data-cellnumber]")

        self.logger.debug("Extracting the numbers and their corresponding elements")
        cell_elements = []
        for cell in cell_divs:
            cell_number = int(cell.get_attribute("data-cellnumber"))
            self.logger.debug(f"Found cell with number: {cell_number}")
            cell_elements.append((cell_number, cell))

        self.logger.debug("Sorting the elements based on the numbers")
        cell_elements.sort(key=lambda x: x[0])

        self.logger.debug("Clicking the elements in ascending order")
        for _, element in cell_elements:
            element.click()

    def perform_test(self) -> None:
        try:
            self.click_start()
            while True:
                self.process_cells()
                self.click_continue_button()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
