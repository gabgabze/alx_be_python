import unittest

from simple_calculator import SimpleCalculator

""" let us write the test from the base TestCase class"""

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 2), -2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 2), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 3), 0.666)
        self.assertEqual(self.calc.divide(-1, 1), 1)
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertEqual(self.calc.divide(0, 0), 'Not Possible')
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(0, 1), 0)