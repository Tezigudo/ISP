from enum import Enum


class PizzaSize(Enum):
    small = 120
    medium = 200
    large = 300

    @property
    def price(self):
        return self.value

    def __repr__(self) -> str:
        return self.name

    __str__ = __repr__


class SaladSize(Enum):
    small = 25
    large = 40

    @property
    def price(self):
        return self.value

    def __repr__(self) -> str:
        return self.name

    __str__ = __repr__


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size):
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        if self.size not in PizzaSize:
            raise ValueError(f"Unknown pizza size {self.size}")
        return self.size.price + 20 * len(self.toppings)

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __repr__(self) -> str:
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = str(self.size)
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain cheese pizza"
        return description

    __str__ = __repr__


class Salad:
    """Mixed vegetable salad, in two sizes."""

    def __init__(self, size):
        """Salad can be small or large."""
        if size not in list(SaladSize):
            raise ValueError("Size must be small or large")
        self.size = size

    def get_price(self):
        """Price of a salad depends only on size."""
        return self.size.price
