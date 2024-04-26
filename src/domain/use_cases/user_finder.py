""" UserFinder use case class """

# pylint: disable=R0903

from abc import ABC, abstractmethod
from typing import Dict


class UserFinder(ABC):
    """UserFinder use case abstract class"""

    @abstractmethod
    def find(self, first_name: str) -> Dict:
        """Find user by first_name"""
        raise NotImplementedError("Method not implemented")


# class UserFinderUseCase(UserFinder):
#    """UserFinder use case"""
#
#    def find(self, first_name: str) -> Dict:
#        """Find user by first_name"""
#        pass
