# Test Automation Project
This is test automation project based on `Selenium-Webdriver` with Python. It's still developing package of automated tests of [JioCinema.com](https://www.jiocinema.com/) website.

## Automation
Automation describes a wide range of technologies that reduce human intervention in processes, namely by predetermining decision criteria, subprocess relationships, and related actions, as well as embodying those predeterminations in machines. Automation has been achieved by various means including mechanical, hydraulic, pneumatic, electrical, electronic devices, and computers, usually in combination. Complicated systems, such as modern factories, airplanes, and ships typically use combinations of all of these techniques. The benefit of automation includes labor savings, reducing waste, savings in electricity costs, savings in material costs, and improvements to quality, accuracy, and precision.

## Why do we need to log the events?
Logging can simply record the entire test session in a file, including the results of assert actions that can indicate which tests cases are passed and which ones are failed. Therefore, we can have a clean helpful report for tests, which can then be presented to, e.g., development teams.

To log events, first of all, we need to have an API that defines the codes that are executed every time a certain Selenium driver action is executed - for instance, whenever we execute `driver.find_element()`. The code executed every time a Selenium code is executed can be a logging code. Therefore, and second, we also need an API (or a few lines of code) that records or logs something. Refer [helpers](src/helpers/web_driver_listener.py)

For the first API, Selenium has provided the class EventFiringWebDriver that can be imported through `from selenium.webdriver.support.events import EventFiringWebDriver`. This class wraps/bundle another object, of type AbstractEventListener, around/with well-known webdriverobject. However, we do not directly use AbstractEventListener class, because it is an abstract/ancestor class that needs to be inherited in order to be used (equivalent to interfaces in Java). Therefore, after importing AbstractEventListener class through `from selenium.webdriver.support.events import AbstractEventListener` , we need to inherit a class from it, where we define the arbitrary codes that we want to be executed along with webdriver events. The code block below shows a simple inheritance of AbstractEventListener with single defined method that activates once we execute get method of webdriver.
```
from selenium.webdriver.support.events import AbstractEventListener
class AnEventListener(AbstractEventListener):
    def after_navigate_to(self, url, driver):
        # Writing url to a file 
```
Here, we can use the logger object above in our AbstractEventListener implementation.

## Getting Started for setup


# Project Structure

├── [src](./src/)
    │
    ├── [base](./src/base/)                         
    │       ├── [base_page.py](./src/base/base_page.py)         
    |  
    ├── [extensions](./src/extensions/)                       
    │       ├── [web_driver_extended.py](./src/extensions/web_deriver_extended.py)     
    │   
    ├── [helpers](./src/helpers/) 
    |       ├── [web_driver_listener.py](./src/helpers/web_driver_listener.py)
    |
    ├── [locators](./src/locators/)                            
    │       ├── [locators_elements.py](./src/locators/locators_elements.py)   
    |
    ├── [logs](./src/logs/)          
    |       ├── *.log
    |
    ├── [pages](./src/pages/)                 
    |       ├── [home_page.py](./src/pages/home_page.py)     
    |       ├── [movies_page.py](./src/pages/movies_page.py)
    |       ├── [search_page.py](./src/pages/search_page.py)      
    |
    ├── [reports](./src/reports/)                   
    |       ├── [archive](./src/reports/archive/)  
    |       |       ├── *.json
    |       ├── [output.json](./src/reports/output.json)
    |       ├── [pytest_html_report.html](./src/reports/pytest_html_report.html)   
    |
    ├── [utils](./src/utils/)                 
    |       └── [utils.py](./src/utils/utils.py)
    

├── [tests](./tests/)
    │
    ├── [conftest.py](./tests/conftest.py)
    ├── [test_base.py](./tests/test_base.py)
    ├── [test_home_page.py](./tests/test_home_page.py)
    ├── [test_movies_page.py](./tests/test_movies_page.py)
    └── [test_search_page.py](./tests/test_search_page.py)


Here you can find a short description of main directories and it's content

- [base](src/base/) - we used for opening base url.
- [extensions](src/extensions/) - A wrapper around an arbitrary WebDriver instance which supports firing events.
- [helpers](src/helpers/) - is more of a place where you store code architectural snippets in my view. Things essential for bootstrapping components.
- [locators](src/locators/) - there are locators of web elements in locators_elements.py grouped in classes
- [pages](src/pages/) - there are sets of method for each test step (notice: some repeated methods were moved to [utils.py](src/utils/utils.py))
- [logs](src/logs/) - you will find day by day logs generates.
- [reports](src/reports/) - if you run tests with html-reporter, tests reports will be saved in this directory [reports](src/reports/pytest_html_report.html)
- [utils](src/utils/) - this directory contains files responsible for configuration, e.g. driver_factory.py for webdriver management
- [tests](./tests/) - there are sets of tests for main functionalities of website

# Project Features
- framework follows `Page Object Pattern`.
- logger has been implemented.
```
def after_click(self, element, driver):
    if element.get_attribute("text") is None:
        self.log.info(f"{element.get_attribute('class')} clicked")
    else:
        self.log.info(f"{element.get_attribute('text')} clicked")
```
- the ability to easily generate legible and attractive test reports using `html-reporter`.
- tests can be run on popular browsers - Chrome and Edge are preconfigured in `class DriverFactory` and both can be select in [conftest.py](./tests/conftest.py), e.g.
```
@pytest.fixture(scope='class')
def setup(request):
    web_driver = DriverFactory.get_config_web_driver("chrome")
```

# SetUp Environment
1. Install virtualenv package
```
$ pip install virtualenv
```

2. Create virtualenv folder
```
$ python -m virtualenv venv
```

3. Activate venv
```
$ venv\Scripts\activate 
```
(OR) 
```
$ source venv/Scripts/activate
```

If mac
```
$ source venv/bin/activate
```

4. Install all packeage required for the project
```
$ pip install -r requirements.txt
```

5. create `.env` and set your username refer [env_sample](./env_sample)(`Note:` If we are using edge browser without cognito_mode we have to set EDGE_USERNAME in `.env` file)
```
    EDGE_USERNAME = 'your.name'
```

## Run testcases
For the metadata will be displayed in the terminal report header
```
$ pytest -v
```

For display all print statements
```
$ pytest -s
```

For running tests using expression
```
$ pytest -k test_home
```

For running test using marker
```
$ pytest -m regression
```
```
$ pytest -m smoke
```

## More commands
Use the `--durations` option to the pytest command to include a duration report in your test results. `--durations` expects an integer value n and will report the slowest n number of tests.
```
$ pytest --durations=10
```

It will used for display print statements
```
$ pytest -s
```

Run tests by marker expressions
```
$ pytest -m smoke
```

## Pytest Plugins
If you want to measure how well your tests cover your implementation code, then you can use the coverage package. `pytest-cov` integrates coverage, so you can run `pytest --cov` to see the test coverage report and boast about it on your project front page.
```
$ pip install pytest-cov
```
Run generating coverage
```
$ pytest --cov
```

If not installed allure in windows
open powershell and execute commands
```
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
> irm get.scoop.sh | iex
> scoop install allure
```

If not installed allure in mac
```
$ brew install allure
```
pytest plugin for generating allure HTML reports
```
$ pip install allure-pytest
```
Run generate report folder by `--alluredir`
```
$ pytest --alluredir=src/reports
```
To serve the allure report by <report_folder_path>
```
allure serve src/reports
```

With this call, pytest will spawn a number of `--workers` processes equal to the number of available CPUs, and distribute the tests randomly across them.
```
$ pip install pytest-xdist
```
For creating multiple threads
```
$ pytest -n auto
```
(OR)
```
$ pytest -n 4
```

```
pip install pytest-dotenv
```
```
pip install pytest-junit
```