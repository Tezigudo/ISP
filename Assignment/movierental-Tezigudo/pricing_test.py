import unittest

from customer import Customer
from rental import Rental
from movie import Movie
from pricing import PriceCode


class PricingTest(unittest.TestCase):

    def setUp(self) -> None:

        self.customer = Customer('Fred')
        self.movie0 = Movie('The Matrix', 1999, ['Action', 'Sci-Fi'])
        self.rental0 = Rental(self.movie0, 3)
        self.movie1 = Movie('Tom and Jerry', 2019, ['Children', 'Cartoon'])
        self.rental1 = Rental(self.movie1, 3)
        self.movie2 = Movie('The Godfather', 2022, ['Drama'])
        self.rental2 = Rental(self.movie2, 3)

    def test_regular_price(self) -> None:
        self.assertEqual(self.rental0.get_price(), 3.5)

    def test_childrens_price(self) -> None:
        self.assertEqual(self.rental1.get_price(), 1.5)

    def test_new_release_price(self) -> None:
        self.assertEqual(self.rental2.get_price(), 9.0)
