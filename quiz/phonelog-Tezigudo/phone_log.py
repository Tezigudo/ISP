"""
PhoneLog keeps a record of received phone calls,
in reverse cronological order (most recent call first).
For each distinct phone number, it keeps only the most
recent call to/from that phone number.

PhoneLog has a capacity that is the maximum number of phone
numbers it will save. This capacity is for the number of saved
numbers, not including the parameter to any methods.
When the PhoneLog is full and a new (distinct) number is received,
the oldest value is removed.
A phone number can be any non-empty, non-whitespace string
(not just digits).  Leading and trailing whitespace are removed
from phone numbers before saving them.
"""


class PhoneLog:

    def __init__(self, capacity: int):
        """Initialize a new PhoneLog object.

        :param capacity:  the maximum number of distinct phone numbers to save.
        """
        # don't test this.  It's too trivial.
        if not isinstance(capacity, int):
            raise TypeError("capacity must be a positive integer")
        self.__capacity = capacity
        self.__calls = []

    @property
    def capacity(self):
        """The maximum number of distinct phone numbers that can be saved."""
        return self.__capacity

    def get_calls(self):
        """Return a list of phone numbers in the phonelog.

        :returns: list of phone numbers, most recently received number first
        """
        return self.__calls

    def record_call(self, phone_number: str):
        """Add a phone number to the call log.

        If the phone number is already in the phone log,
        then move it to the start of the list (most recent call).
        If the phone number is not in the phone log, then add it
        to the beginning, and (if necessary) remove the oldest number
        to make space.

        :param phone_mumber: a phone number to record.  Leading and trailing
             white space is removed before saving the number.
        :raises ValueError: if the `phone_number` is empty or only whitespace.
        """
        phone_number = phone_number.strip()
        if len(phone_number) == 0:
            raise ValueError("phone_number may not be empty or whitespace")

        # if full then make space
        if len(self.__calls) >= self.capacity:
            self.__calls.pop()
        # remove any duplicate
        try:
            self.__calls.remove(phone_number)
        except ValueError:
            pass
        self.__calls.insert(0, phone_number)
