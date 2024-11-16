import pytest
import allure
import json
import copy
import logging

from allure_commons.types import AttachmentType
from pathlib import Path
from constants import (
    DEFAULT_URL,
    SUPPORTED_BROWSERS,
    DEFAULT_WAIT_TIME
)
from src.utils.driver_factory import DriverFactory
from src.utils.config_file import Config

@pytest.fixture(scope="session", autouse=True)
def project_root() -> Path:
    """The Project (or Workspace) root as a filepath.

    * This conftest.py file should be in the Project Root if not already.
    """
    return Path(__file__).absolute().parent

@pytest.fixture(scope="session")
def _load_config_json(project_root, request) -> Config:
    """Load the default config.json file or the given config.json config file (if specified).

    * config looks for these files from the Project Root!

    I may have multiple config.json files with different presets. For example:
    - stage-config.json
    - dev-testing.json
    - firefox-config.json

    Examples
    --------
    $ pytest
    >>> Loads the default file: PROJECT_ROOT/config.json

    $ pytest config_json=dev-config.json
    >>> Loads the config file: PROJECT_ROOT/dev-config.json

    $ pytest config_json="configs/stage-config.json"
    >>> Loads the config file: PROJECT_ROOT/configs/stage-config.json
    """
    custom_config_filepath = request.config.getoption("config_json")
    config_filepath = project_root.joinpath(custom_config_filepath or "config.json")

    try:
        with config_filepath.open() as file:
            _json = json.load(file)
        config = Config(**_json)
    except FileNotFoundError:
        logging.warning(f"The config_filepath was not found, so Config will load with default values. File not found: {config_filepath.absolute()}")
        config = Config()

    return config


@pytest.fixture(scope="session")
def _override_config_config_values(_load_config_json: Config, request) -> Config:
    """Override any Config values after loading the initial config.json config file.

    After a config.json config file is loaded and converted to a Config object,
    then any CLI arguments override their respective key/values.
    """
    config = _load_config_json
    # Driver Settings
    cli_remote_url = request.config.getoption("--remote_url")
    if cli_remote_url:
        config.driver.remote_url = cli_remote_url

    cli_browser_options = request.config.getoption("--options")
    if cli_browser_options:
        config.driver.options = [option.strip() for option in cli_browser_options.split(",")]

    cli_browser = request.config.getoption("--browser")
    if cli_browser:
        config.driver.browser = cli_browser

    cli_local_path = request.config.getoption("--local_path")
    if cli_local_path:
        config.driver.local_path = cli_local_path

    cli_capabilities = request.config.getoption("--caps")
    if cli_capabilities:
        # --caps must be in '{"name": "value", "boolean": true}' format
        # with double quotes around each key. booleans are lowercase.
        config.driver.capabilities = json.loads(cli_capabilities)

    cli_wire_enabled = request.config.getoption("--wire_enabled")
    if cli_wire_enabled:
        # --wire_enabled is false unless they specify "true"
        wire_enabled = cli_wire_enabled.lower() == "true"
        config.driver.seleniumwire_enabled = wire_enabled

    cli_wire_options = request.config.getoption("--wire_options")
    if cli_wire_options:
        # --wire_options must be in '{"name": "value", "boolean": true}' format
        # with double quotes around each key. booleans are lowercase.
        config.driver.seleniumwire_options = json.loads(cli_wire_options)

    cli_page_wait_time = request.config.getoption("--page_load_wait_time")
    if cli_page_wait_time and cli_page_wait_time.isdigit():
        config.driver.page_load_wait_time = int(cli_page_wait_time)

    # Logging Settings
    cli_screenshots_on = request.config.getoption("--screenshots_on")
    if cli_screenshots_on:
        shots_on = cli_screenshots_on.lower() == "true"
        config.logging.screenshots_on = shots_on

    cli_extensions = request.config.getoption("--extensions")
    if cli_extensions:
        config.driver.extension_paths = [ext.strip() for ext in cli_extensions.split(",")]

    cli_log_level = request.config.getoption("--pylog_level")
    if cli_log_level:
        level = cli_log_level.upper()
        config.logging.pylog_level = level if level in ["DEBUG", "COMMAND", "INFO", "USER", "WARNING", "ERROR", "CRITICAL"] else "INFO"

    return config


@pytest.fixture(scope="function")
def py_config(_override_config_config_values) -> Config:
    """Get a fresh copy of the Config for each test

    See _load_config_json and _override_config_config_values for how the initial configuration is read.
    """
    return copy.deepcopy(_override_config_config_values)


@pytest.fixture(scope="class")
def pyc_config(_override_config_config_values) -> Config:
    """Get a fresh copy of the Config for each test class"""
    return copy.deepcopy(_override_config_config_values)


@pytest.fixture(scope="session")
def pys_config(_override_config_config_values) -> Config:
    """Get a fresh copy of the Config for each test session"""
    return copy.deepcopy(_override_config_config_values)


# @pytest.fixture(scope='session')
# def config():
#     config_file = open(CONFIG_PATH)
#     return json.load(config_file)


@pytest.fixture(scope="session", autouse=True)
def browser_setup(pys_config: Config):
    config = pys_config
    if "browser" in config.driver:
        raise Exception('The config file does not contain "browser"')
    elif config.driver.browser not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config.driver.browser}" is not a supported browser')
    return config.driver.browser


@pytest.fixture(scope='session')
def wait_time_setup(pys_config: Config):
    config = pys_config
    return config.driver.wait_time if 'wait_time' in config.driver else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(pys_config: Config):
    config = pys_config
    return config.custom.get('base_url') if "base_url" in config.custom.keys() else DEFAULT_URL


@pytest.fixture(scope='session')
def setup(request, pys_config: Config):
    """
    This function sets up the web driver and implicitly waits for the specified amount of time.
    It then attaches the web driver to the test class and takes a screenshot if the test fails.
    Finally, it quits the web driver.
    """
    config = pys_config
    web_driver = DriverFactory.get_config_web_driver(config)
    web_driver.implicitly_wait(config.driver.wait_time)

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver", web_driver)

    # request.cls.driver = web_driver
    before_failed = request.session.testsfailed

    yield

    if request.session.testsfailed != before_failed:
        allure.attach(web_driver.get_screenshot_as_png(),
                      name="Test failed", attachment_type=AttachmentType.PNG)

    web_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="", help="The lowercase browser name: chrome | firefox")
    parser.addoption("--local_path", action="store", default="", help="The filepath to the local driver")
    parser.addoption("--remote_url", action="store", default="", help="Grid URL to connect tests to.")
    parser.addoption("--screenshots_on", action="store", default="", help="Should screenshots be saved? true | false")
    parser.addoption(
        "--config_json",
        action="store",
        default="",
        help="The filepath of the config.json file to use (ie dev-config.json)",
    )
    parser.addoption(
        "--pylog_level", action="store", default="INFO", help="Set the logging level: 'DEBUG' | 'COMMAND' | 'INFO' | 'USER' | 'WARNING' | 'ERROR' | 'CRITICAL'"
    )
    parser.addoption(
        "--options",
        action="store",
        default="",
        help='Comma-separated list of Browser Options. Ex. "headless, incognito"',
    )
    parser.addoption(
        "--caps",
        action="store",
        default="",
        help='List of key-value pairs. Ex. \'{"name": "value", "boolean": true}\'',
    )
    parser.addoption(
        "--page_load_wait_time",
        action="store",
        default="",
        help="The amount of time to wait for a page load before raising an error. Default is 0.",
    )
    parser.addoption("--extensions", action="store", default="", help='Comma-separated list of extension paths. Ex. "*.crx, *.crx"')
    parser.addoption(
        "--wire_enabled",
        action="store",
        default=False,
        help="Should the Wire Protocol be enabled? true | false",
    )
    parser.addoption(
        "--wire_options",
        action="store",
        default="",
        help='Dict of key-value pairs as a string. Ex. \'{"name": "value", "boolean": true}\'',
    )

