""" Spy test para UserFinder """

from typing import Dict


class UserFinderSpy:
    """Spy class para UserFinder"""

    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, first_name: str) -> Dict:
        """Spy para o metodo find"""

        self.find_attributes["first_name"] = first_name

        response = {
            "type": "Users",
            "count": 1,
            "attributes": [{"first_name": first_name, "last_name": "last", "age": 43}],
        }

        return response
