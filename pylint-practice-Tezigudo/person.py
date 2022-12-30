"""This module contain Person class that have name and birthday."""

from datetime import date
today = date.today()


class Person:
    """a person with a name and a birthday.

    Example:
    >>> p = Person("Hacker")
    >>> p.name
    'Hacker'
    >>> p.age
    0
    >>> p.set_birthday(2001, 1, 1)
    >>> p.age
    21
    >>> str(p)
    'young adult named Hacker'
    >>> p.set_birthday(2002,12,31)
    >>> p.age
    19
    >>> str(p)
    'teenager named Hacker'
    """

    def __init__(self, name, birthday=date.today()):
        """Initialize a Person.

        Arguments:
            name {str} -- name of person

        Keyword Arguments:
            birthday {datetime.date} -- birthdate(default: {date.today()})

        Raises:
            TypeError: if user not initialize name with an string
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name
        self.birthday = birthday

    @staticmethod
    def youthfulness(person):
        """Comment based on a person's age."""
        status = None
        if person.age < 0:
            status = "unborn"
        elif person.age < 1:
            status = "baby"
        elif person.age < 6:
            status = "child"
        elif person.age < 13:
            status = "youth"
        elif person.age < 20:
            status = "teenager"
        elif person.age < 30:
            status = "young adult"
        elif person.age < 60:
            status = "middle-ager"
        elif person.age < 80:
            status = "senior"
        elif person.age < 90:
            status = "octogenarian"  # someone 80-89
        elif person.age < 90:
            status = "nonagenarian"  # someone 90-99
        else:
            status = "centenarian"  # someone >= 100, aka "centarian"
        return status

    def __str__(self):
        """Implement string function."""
        return Person.youthfulness(self) + " named " + self._name

    def set_birthday(self, year: int, month: int, day: int):
        """Set birthday to person."""
        self.birthday = date(year, month, day)

    @property
    def age(self) -> int:
        """Get the age of person."""
        birth = self.birthday
        age = today.year - birth.year
        if (birth.month, birth.day) > (today.month, today.day):
            # this year's birthday has not occurred yet
            age -= 1
        return age

    @property
    def name(self) -> str:
        """Get name of this person."""
        return self._name

    def __eq__(self, other):
        """Two people are considered to be equal \
        if they have the same name and the same birthday."""
        if not isinstance(other, Person):
            return False
        return self._name == other._name and self.birthday == other.birthday
