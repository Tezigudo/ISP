"""Check is a claim for a specified about of Money, with a serial number."""
from money import Money


class Check(Money):
    """
    A check with a value and an auto-generated serial number.
    Check is a form of Money, so you can add Checks and Money.
    The result of add (+) is always Money.
    If you compare Checks using == it will compare the value,
    currency, AND the serial number.  So two Check objects
    are equal only if value, currency, and serial number are same.

    >>> c = Check(5000)
    >>> c.value
    5000
    >>> c.check_number    # get the check serial number
    1000000
    >>> str(c)
    'Check number 1000000 for 5,000.00 Baht'
    >>> m = Money(200)
    >>> str(c+m)           # addition is inherited from Money
    '5,200.00 Baht'
    >>> c > m
    True
    >>> c2 = Check(c.value)
    >>> c == c2            # not same. Check number is different
    False
    """
    # Class attribute to remember next available serial number.
    _next_check_number = 1000000

    def __init__(self, amount: float):
        """A new check with a given amount.

        Check number is assigned automatically.
        Args:
            amount - value of this check
        """
        if amount < 0:
            raise ValueError("Check value cannot be negative.")
        super().__init__(amount)
        self.__number = Check._next_check_number
        Check._next_check_number += 1

    @property
    def check_number(self):
        """Get the check number."""
        return self.__number

    def __eq__(self, other):
        """Two checks are equal if they have same value and check number."""
        if not isinstance(other, Check):
            return False
        return self.check_number == other.check_number and self.value == other.value

    def __str__(self):
        return f"Check number {self.__number:d} for {super().__str__()}"

    def __repr__(self):
        return f"Check({self.value})"
