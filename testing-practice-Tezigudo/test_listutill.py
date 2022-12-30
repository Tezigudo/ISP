import unittest
from listutil import unique


class TestUnique(unittest.TestCase):

    def test_Empty(self):
        """test whether be a empty list"""
        self.assertListEqual([], unique([]))

    def test_no_param(self):
        """test no parameter in function TypeError must be raise"""
        with self.assertRaises(TypeError):
            unique()

    def test_wrong_param_type(self):
        """test that if parameter isn't list it will raise TypeError"""
        with self.assertRaises(TypeError):
            unique('5')

        with self.assertRaises(TypeError):
            unique(5)

        with self.assertRaises(TypeError):
            unique(True)

    def test_one_element(self):
        """testing one element in the list
           it must return that elenent"""
        self.assertListEqual([4], unique([4]))

    def test_oridinary_case(self):
        """testing the oridinart case that should work"""
        self.assertListEqual([1, 2, 3, 'a'], unique(
            [1, 1, 2, 1, 3, 2, 1, 3, 'a']))
