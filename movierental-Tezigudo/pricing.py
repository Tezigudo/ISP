from abc import ABC, abstractmethod
from enum import Enum


class PriceCode(Enum):
    """The following are the different price codes."""
    new_release = {"price": lambda days: 3.0*days, "frp": lambda days: days}
    regular = {"price": lambda days: 2.0 + 1.5 *
               (days-2) if days > 2 else 2, "frp": lambda days: 1}
    childrens = {"price": lambda days: 1.5 + 1.5 *
                 (days-3) if days > 3 else 1.5, "frp": lambda days: 1}

    def get_price(self, days: int) -> float:
        """Return rental price for a given number of days."""
        pricing = self.value["price"]  # a lambda
        return pricing(days)

    def get_rental_points(self, days: int) -> int:
        """Return rental points for a given number of days."""
        point_calculating = self.value["frp"]
        return point_calculating(days)

    def __repr__(self) -> str:
        return self.name
    __str__ = __repr__
