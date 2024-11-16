import logging
import datetime
from selenium.webdriver.support.events import AbstractEventListener


class WebDriverListener(AbstractEventListener):
    log_filename = datetime.datetime.now().strftime("%Y%m%d")
    logging.basicConfig(
        # log file will be created in "src/logs" directory. Feel free to change the path or filename
        filename=f"src/logs/{log_filename}.log",
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
    )

    def __init__(self):
        self.log = logging.getLogger("selenium")

    def before_navigate_to(self, url, driver):
        self.log.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.log.info(f"{url} opened")

    def before_find(self, by, value, driver):
        self.log.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.log.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.log.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.log.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.log.info(f"{element.get_attribute('class')} clicked")
        else:
            self.log.info(f"{element.get_attribute('text')} clicked")

    def before_change_value_of(self, element, driver):
        self.log.info(f"{element.get_attribute('text')} value changed")

    def after_change_value_of(self, element, driver) -> None:
        self.log.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver):
        self.log.info("Driver quitting")

    def after_quit(self, driver):
        self.log.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.log.info(exception)
