"""
Overload the operators > and >= and you get < and <= for free,
since Python automatically reverses direction of comparison
when only one operator is explicitly overloaded.
"""


class Money:
    """
    Money is an immutable object with a value and currency.
    For this application the currency is fixed as Baht,
    so don't mess with it.

    You can add Money objects that have the same currency, 
    including Checks (a subclass) and the result is Money.
    You can compare Money using ==, so you can write:
    ```
    total = Money(500) + Money(100)
    total == Money(600)   # True
    ```

    >>> m = Money(1000)
    >>> m.value
    1000
    >>> m.currency
    'Baht'
    >>> m2 = m + Money(100)
    >>> str(m2)
    '1,100.00 Baht'
    >>> m2   # invokes m2.__repr__()
    Money(1100, 'Baht')
    >>> m2 > m
    True
    >>> m2 = m2 - Money(100)
    >>> m == m2
    True
    """
    def __init__(self, value: float, currency: str = 'Baht'):
        """Initialize a new money object with given value."""
        self.__value = value
        self.__currency = currency

    @property
    def value(self) -> float:
        """The value of this Money, as a number."""
        return self.__value

    @property
    def currency(self) -> str:
        """The currency of this Money object."""
        return self.__currency

    def __add__(self, money):
        """Add a money object to this one and return the sum."""
        return Money(self.__value + money.__value, self.currency)

    def __sub__(self, money):
        """Subtract a money object to this one and return the difference."""
        return Money(self.__value - money.__value, self.currency)

    def __gt__(self, money):
        """Compare money objects by value, ignoring currency.

        >>> m = Money(100)
        >>> m2 = Money(101)
        >>> m > m2
        False
        >>> m2 > m
        True
        """
        return self.__value > money.__value

    def __ge__(self, money):
        """
        >>> m = Money(100)
        >>> m2 = Money(101)
        >>> m >= m2
        False
        >>> m2 >= m
        True
        >>> m >= m
        True
        """
        return self.__value >= money.__value

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        # ignore currency, use value properties
        return self.value == other.value

    def __str__(self):
        return f"{self.value:,.2f} {self.__currency}"

    def __repr__(self):
        return f"Money({self.value}, '{self.__currency}')"
