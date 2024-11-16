import pytest
from dotenv import load_dotenv
load_dotenv()

@pytest.mark.usefixtures('setup')
class TestBase:
    pass