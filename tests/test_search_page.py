import pytest
import allure
import string
import time

from collections.abc import Iterable
from src.pages.search_page import SearchPage
from tests.test_base import TestBase
from src.locators.locators_elements import (
    SearchPageLocators,
    HomePageLocators
)
from constants import (
    SEARCH_PATH
)


@allure.suite("suite name")
@pytest.mark.smoke
class TestSearchPage(TestBase):
    """
        test search_page.py
    """

    @pytest.fixture
    def setUp(self):
        self.search_movie = SearchPage(driver=self.driver)

    @allure.title("""Search movie and verify with movie title""")
    @allure.description("""
        1. open search page
        2. send movie name into search input
        3. select top list one from movies results
        4. click on watch button
        5. get movie title
    """)
    @allure.severity(allure.severity_level.BLOCKER)
    def test_search_movie_and_verify_with_movie_title(self, setUp):
        # init
        movie_name = 'Roohi'

        # testcases
        self.search_movie.open(path=SEARCH_PATH)
        self.search_movie.send_movie_name_to_search(search_movie_name=movie_name)

        # # assert statement
        # assert self.driver.find_element(*SearchPageLocators.search_box).get_attribute("value") == movie_name

        # # testcase
        # self.search_movie.select_top_list_movie_and_open()
        # self.search_movie.click_on_watch_button()

        # # digits are mapped to None
        # translation_table = str.maketrans('', '', string.digits)

        # # assert statements
        # assert self.driver.find_element(*HomePageLocators.movies_link).text.strip().lower() == 'Free'.lower()
        # assert self.driver.find_element(*HomePageLocators.movies_link).is_enabled() == True
        # assert self.driver.find_element(*HomePageLocators.movies_link).is_displayed() == True
        # assert (self.search_movie.get_movie_title()).translate(translation_table).strip(
        # ).lower() == movie_name.translate(translation_table).strip().lower()

    def test_verify_suggestions_list_from_search_page(self, setUp):
        # init
        valid_movie_name = 'drishyam'
        invalid_movie_name = 'xyz123'
        empty_list = []

        # testcases

        # passed valid movie name and get suggestions movie list
        self.search_movie.open(path=SEARCH_PATH)
        self.search_movie.send_movie_name_to_search(search_movie_name=valid_movie_name)

        # assert statement
        # assert self.driver.find_element(*SearchPageLocators.search_box) \
        #         .get_attribute("value").strip().lower() == valid_movie_name.lower()

        # valid_list_of_suggestions = self.search_movie.get_suggestions_list_dropdown_from_search()

        # # passed invalid movie name and get No Result found
        # self.search_movie.open(path=SEARCH_PATH)
        # self.search_movie.send_movie_name_to_search(search_movie_name=invalid_movie_name)

        # # assert statement
        # assert self.driver.find_element(*SearchPageLocators.search_box) \
        #         .get_attribute("value").strip().lower() == invalid_movie_name.lower()

        # no_results_found = self.search_movie.get_suggestions_list_dropdown_from_search()

        # # assert statements
        # assert valid_list_of_suggestions != empty_list
        # assert no_results_found == empty_list
