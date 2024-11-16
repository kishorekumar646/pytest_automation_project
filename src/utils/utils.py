import time


class Utils:
    "Utils logic applied here"

    def __init__(self) -> None:
        pass

    def sending_characters_in_search(self, web_element, string):
        for character in string:
            web_element.send_keys(character)
            time.sleep(0.10)
