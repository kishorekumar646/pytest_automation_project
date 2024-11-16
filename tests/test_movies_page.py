import pytest
import allure
import time

from selenium.common.exceptions import (
    NoSuchElementException
)
from tests.test_base import TestBase
from src.pages.movies_page import MoviePage
from src.locators.locators_elements import (
    VideoPageLocators
)
from constants import (
    MOVIES_PATH
)

@allure.suite("suite name")
@pytest.mark.regression
class TestMoviesPage(TestBase):
    """
        test movies_page.py
    """

    @pytest.fixture
    def setUp(self):
        self.movie_page = MoviePage(driver=self.driver)

    @allure.title("Test mute and unmute video and change video resolution")
    @allure.description("verify mute and unmute and change the video resolution")
    def test_verify_mute_and_unmute_video_and_change_video_resolution(self, setUp):
        # init
        unmute_text = 'Unmute'
        mute_text = 'Mute'
        resolution_text = 'Resolution'
        standard_text = 'Standard'

        # testcases
        self.movie_page.open(path=MOVIES_PATH)
        self.movie_page.click_watch_button_from_selected_movie()

        # # mute video
        self.movie_page.mute_while_playing_video()

        # # assert statement should have attr value UnMute after click mute button
        # print(self.driver.find_element(*VideoPageLocators.unmute_button).get_attribute("aria-label").strip().lower())
        assert self.driver.find_element(*VideoPageLocators.unmute_button).get_attribute("aria-label").strip().lower() == unmute_text.lower()

        # # unmute video
        # self.movie_page.unmute_while_playing_video()

        # # assert statement should have attr value Mute after click unmute button
        # assert self.driver.find_element(*VideoPageLocators.mute_button).get_attribute("aria-label").strip().lower() == mute_text.lower()

        # # clike on settings
        # self.movie_page.click_movie_video_settings()

        # # assert statement should click and return attr value Resolution
        # assert self.driver.find_element(*VideoPageLocators.settings_button) \
        #         .get_attribute("aria-label").strip().lower() == resolution_text.lower()

        # # change video quality to standard
        # self.movie_page.change_settings_video_quality_to_standard()

        # # assert statement should click to standard and should have text Standard
        # assert self.driver.find_element(*VideoPageLocators.resolution_standard).text.strip().lower() == standard_text.lower()
        time.sleep(10)
