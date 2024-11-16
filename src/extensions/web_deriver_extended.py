from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from constants import (
    DEFAULT_URL
)


class WebDriverExtended(EventFiringWebDriver):
    def __init__(self, driver, event_listener, config):
        super().__init__(driver, event_listener)
        self.base_url = config["base_url"] if "base_url" in config else DEFAULT_URL

    def open(self, path):
        if path is not None:
            self.get(self.base_url + path)
        else:
            self.get(self.base_url)