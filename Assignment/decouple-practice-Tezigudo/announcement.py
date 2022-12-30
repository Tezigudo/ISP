"""Exercise in externalizing data using python-decouple.

   What values to you think should be externalized?
   Look for things that may change.
   Put their values in a .env file and substitute
   variables (read using decouple) for hard-coded constants.
"""

from typing import List
from decouple import config, Csv


def announce_class(is_online: bool, meet_url: str, time: str, room: str):
    """Announce whether class is online, and print the Google Meet link."""
    if is_online:
        print("Class will meet online.")
        print(f"The Google Meet URL is {meet_url}")
    else:
        print("Class will meet at Kasetsart University.")
        print(f"Location is CPE room {room}")
    # time is the same in both cases
    print(f"Class meets {time}\n")


def describe_topics(topics: List[str]):
    """List a list of topics to cover, one per line."""
    print("Topics we will discuss are:")
    for topic in topics:
        print(" -", topic)


if __name__ == '__main__':
    # Does class meet online (True) or at KU (False)?
    IS_ONLINE = config('CLASS_ONLINE', cast=bool, default=False)
    TIME = config('CLASS_TIME', cast=str, default='10:00-11:30')
    MEET_URL = config('MEET_URL', cast=str,
                      default='https://meet.google.com/lookup/abc123')
    TOPICS = config('TOPICS', cast=Csv(), default="TBA")
    ROOM = config('ROOM', cast=str, default='204')

    announce_class(IS_ONLINE, MEET_URL, TIME, ROOM)
    # print a list of today's topics
    describe_topics(TOPICS)
