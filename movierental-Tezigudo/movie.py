
from typing import Collection
from pricing import PriceCode
import csv

MOVIEFILE = 'movie.csv'


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: int, genre: Collection[str]) -> None:
        self.__title = title
        self.__year = year
        self.__genre = genre

    @property
    def title(self) -> str:
        return self.__title

    @property
    def year(self) -> int:
        return self.__year

    @property
    def genre(self) -> Collection[str]:
        return self.__genre

    def is_genre(self, genre: str):
        return genre.lower() in map(str.lower, self.genre)

    def __repr__(self):
        return f"{self.title} ({self.year})"
    __str__ = __repr__

    def get_title(self):
        return self.title


class MovieCatalog:

    def __init__(self) -> None:
        self.movies = []

        with open(MOVIEFILE, 'r') as f:
            reader = csv.reader(f)

            self.movies.extend(Movie(row[1], int(row[2]), row[3].split(
                '|')) for row in reader if not row[0].startswith('#'))

    def get_movie(self, title: str, year: int = -1):
        for movie in self.movies:
            if year == -1:
                if movie.title == title:
                    return movie

            elif movie.title == title and movie.year == year:
                return movie
