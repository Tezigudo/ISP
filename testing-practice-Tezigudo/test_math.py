import unittest
import math


class TestMath(unittest.TestCase):
    """Test of Python math functions."""

    def test_sqrt(self):
        """Test square root of some typical values."""
        self.assertEqual(2, math.sqrt(4))
        self.assertEqual(0, math.sqrt(0))
        self.assertEqual(3e150, math.sqrt(9e300))
        self.assertEqual(1e-100, math.sqrt(1e-200))

    def test_sqareroot_not_equal(self):
        """This test will fail because number are make to be fail"""
        self.assertEqual(-1, math.sqrt(100))

    def test_error_log_of_negative_value(self):
        """Test log of some negative value, this should error"""
        self.assertEqual(-1, math.log(-1))

    def test_log_negative_value(self):
        """testing log(-1) whether it will throw an error"""
        with self.assertRaises(ValueError):
            self.assertEqual(-1, math.log(-1))

    def test_decimal_answer(self):
        """testing all the thing that wll result as a decimal"""
        self.assertAlmostEqual(0.301, math.log10(2), places=3)
        self.assertAlmostEqual(0.477, math.log10(3), places=3)
        self.assertAlmostEqual(2.718281, math.e, delta=0.000001)


if __name__ == "__main__":
    unittest.main()
