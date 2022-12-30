import unittest
from rental import Rental
from pricing import PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie('Mulan', 2022, ['Action', 'Adventure'])
        self.regular_movie = Movie('CitizenFour', 2014, ['Documentary'])
        self.childrens_movie = Movie('Frozen', 2013, ['Animation', 'Family', 'Children'])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", 2014, ['Documentary'])
        self.assertEqual("CitizenFour", m.get_title())
        self.assertEqual(PriceCode.regular, Rental.price_code_for_movie(m))


    def test_rental_price(self):
        """test get_price() for a rental"""
        rental_new_one_day = Rental(self.new_movie, 1)
        rental_new_five_day = Rental(self.new_movie, 5)
        rental_child_one_day = Rental(self.childrens_movie, 1)
        rental_child_five_day = Rental(self.childrens_movie, 5)
        rental_regular_one_day = Rental(self.regular_movie, 1)
        rental_regular_five_day = Rental(self.regular_movie, 5)

        self.assertEqual(rental_new_one_day.get_price(), 3.0)
        self.assertEqual(rental_new_five_day.get_price(), 15.0)
        self.assertEqual(rental_child_one_day.get_price(), 1.5)
        self.assertEqual(rental_child_five_day.get_price(), 4.5)
        self.assertEqual(rental_regular_one_day.get_price(), 2.0)
        self.assertEqual(rental_regular_five_day.get_price(), 6.5)

    def test_rental_points(self):
        """test rental_points() for a rental"""
        rental_new_five_day = Rental(self.new_movie, 5)
        rental_child_five_day = Rental(self.childrens_movie, 5)
        rental_regular_five_day = Rental(self.regular_movie, 5)

        self.assertEqual(rental_new_five_day.rental_points(), 5)
        self.assertEqual(rental_child_five_day.rental_points(), 1)
        self.assertEqual(rental_regular_five_day.rental_points(), 1)
