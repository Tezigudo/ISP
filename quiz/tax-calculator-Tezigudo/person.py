"""Data class for a Person with immutable first_name, last_name,
   and birthdate.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:

    id: str
    first_name: str
    last_name: str

    # constructor with named parameters is auto-generated.

    def __str__(self):
        """Return the person's name."""
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        """Two Persons are considered equal if their id and last_name are the same."""
        if isinstance(other, Person):
            return self.id == other.id and self.last_name == other.last_name
        return False
