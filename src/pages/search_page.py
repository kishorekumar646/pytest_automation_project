import time

from selenium.webdriver.common.keys import Keys
from src.base.base_page import BasePage
from src.utils.utils import Utils
from src.locators.locators_elements import (
    SearchPageLocators,
    VideoPageLocators
)


class SearchPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.util = Utils()

    def send_movie_name_to_search(self, search_movie_name):
        web_element = self.driver.find_element(*SearchPageLocators.search_box)
        self.util.sending_characters_in_search(web_element=web_element, string=search_movie_name)

    def get_suggestions_list_dropdown_from_search(self):
        # here we need to get list of elements so used driver.find_elements
        return self.driver.find_elements(*SearchPageLocators.get_suggestions_list)

    def select_top_list_movie_and_open(self):
        self.driver.find_element(*SearchPageLocators.select_top_list_movie_from_search).send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(
            *SearchPageLocators.select_top_list_movie).click()

    def click_on_watch_button(self):
        self.driver.find_element(
            *SearchPageLocators.open_selected_movie).click()

    def get_movie_title(self):
        return self.driver.find_element(*SearchPageLocators.get_movie_title_name).text

    def pause_video(self):
        self.driver.find_element(*VideoPageLocators.play_button).click()

    def change_video_quality(self):
        self.driver.find_element(*VideoPageLocators.settings_button).click()
