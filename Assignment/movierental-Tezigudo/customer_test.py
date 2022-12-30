import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie('Mulan', 2022, ['Action', 'Adventure'])
        self.regular_movie = Movie('CitizenFour', 2014, ['Documentary'])
        self.childrens_movie = Movie('Frozen', 2013, ['Animation', 'Family', 'Children'])

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace("\n", ""), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_amount(self):
        """test total_amount() for a customer"""
        self.assertEqual(self.c.total_amount(), 0.0)
        self.c.add_rental(Rental(self.new_movie, 4))
        self.assertEqual(self.c.total_amount(), 12.0)

    def test_total_rental_points(self):
        """test total_rental_points() for a customer"""
        self.assertEqual(self.c.total_rental_points(), 0)
        self.c.add_rental(Rental(self.new_movie, 4))
        self.assertEqual(self.c.total_rental_points(), 4)
