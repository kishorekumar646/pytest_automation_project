import time

from selenium.webdriver import ActionChains
from src.base.base_page import BasePage
from src.locators.locators_elements import (
    MoviesPageLocators,
    VideoPageLocators
)

class MoviePage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.actions = ActionChains(self.driver)

    def click_watch_button_from_movies_page(self):
        self.driver.find_element(*MoviesPageLocators.watch_button_from_movies).click()

    def click_watch_button_from_selected_movie(self):
        self.driver.find_element(*MoviesPageLocators.watch_button_for_open_movie).click()

    def mute_while_playing_video(self):
        # return WebDriverWait(driver=self.driver,timeout=35,poll_frequency=35, ignored_exceptions=None).until(EC.visibility_of_all_elements_located((By.XPATH, '//button[@aria-label="Mute"]')))
        self.actions.click(self.driver.find_element(*VideoPageLocators.mute_button)).perform()

    def unmute_while_playing_video(self):
        self.actions.click(self.driver.find_element(*VideoPageLocators.unmute_button)).perform()

    def click_movie_video_settings(self):
        # self.select = Select(*VideoPageLocators.settings_button)
        self.actions.click(self.driver.find_element(*VideoPageLocators.settings_button)).perform()
        # self.driver.find_element(*VideoPageLocators.settings_button).click()

    def change_settings_video_quality_to_standard(self):
        # self.select.select_by_value('Standard')
        self.actions.click(self.driver.find_element(*VideoPageLocators.resolution_standard)).perform()
        # self.driver.find_element(*VideoPageLocators.resolution_standard).send_keys('Sandard', Keys.ENTER)
        
        # return self.driver.find_element(*VideoPageLocators.resolution_standard).text