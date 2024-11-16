import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from src.extensions.web_deriver_extended import WebDriverExtended
from src.helpers.web_driver_listener import WebDriverListener
from src.utils.config_file import Config

USER_NAME = os.getenv('EDGE_USERNAME')


class DriverFactory:
    """
        Configure Selenium Web Driver
    """

    @staticmethod
    def get_config_web_driver(config: Config) -> WebDriverExtended:
        if config.driver.browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging', 'enable-automation'])
            options.add_argument("start-maximized")
            options.add_argument("disable-popup-blocking")

            if str(config.driver.options) in 'headless_mode':
                options.add_argument("--headless=new")

            if str(config.driver.options) in 'cognito_mode':
                options.add_argument("--incognito")

            driver = WebDriverExtended(
                webdriver.Chrome(service=Service(
                    ChromeDriverManager().install()), options=options),
                WebDriverListener(), config
            )

            return driver

        elif config['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")

            if str(config.driver.options) in 'headless_mode':
                options.add_argument("--headless")

            if str(config.driver.options) in 'cognito_mode':
                options.add_argument("--private-window")

            driver = WebDriverExtended(
                webdriver.Firefox(service=Service(
                    GeckoDriverManager().install()), options=options),
                WebDriverListener(), config
            )

            return driver

        elif config['browser'] == 'edge':
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging', 'enable-automation'])
            options.add_argument("start-maximized")

            if str(config.driver.options) in 'headless_mode':
                options.add_argument("--headless=new")

            if str(config.driver.options) in 'cognito_mode':
                options.add_argument("--inprivate")

            else:
                #     options.add_argument("profile-directory=Test Profile")
                options.add_argument(
                    f"user-data-dir=C:/Users/{USER_NAME}/AppData/Local/Microsoft/Edge/User\ Data")
                # options.capabilities['ignoreProtectedModeSettings'] = True
                # options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

            driver = WebDriverExtended(
                webdriver.Edge(service=Service(
                    EdgeChromiumDriverManager().install()), options=options),
                WebDriverListener(), config
            )

            return driver

        elif config['browser'] == 'safari':
            raise NotImplementedError
