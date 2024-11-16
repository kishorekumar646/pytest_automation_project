import time

from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from src.locators.locators_elements import (HomePageLocators)

class HomePage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def navigate_to_movies(self):
        self.driver.find_element(*HomePageLocators.movies_link).click()

    def navigate_to_tv_shows(self):
        self.driver.find_element(*HomePageLocators.tv_shows_link).click()