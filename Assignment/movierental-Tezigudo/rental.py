from datetime import datetime
from movie import Movie
from pricing import PriceCode


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    NEW_RELEASE = PriceCode.new_release
    REGULAR = PriceCode.regular
    CHILDRENS = PriceCode.childrens

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_price(self):
        return Rental.price_code_for_movie(self.movie).get_price(self.days_rented)

    def rental_points(self):
        return Rental.price_code_for_movie(self.movie).get_rental_points(self.days_rented)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    @classmethod
    def price_code_for_movie(cls, movie: Movie) -> PriceCode:
        if movie.year == datetime.now().year:
            return cls.NEW_RELEASE
        if 'Children' in movie.genre or 'Childrens' in movie.genre:
            return cls.CHILDRENS
        return cls.REGULAR
