from src.locators.locators import Locators
from constants import DEFAULT_URL


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        # self.locators = Locators(driver=driver)

    def open(self, path=None):
        self.driver.open(path)
