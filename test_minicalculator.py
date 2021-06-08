import unittest
from main import MiniCalculator


class TestMiniCalculator(unittest.TestCase):

    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 4, "Adding 2 to 2 should equal 4")

    def test_subtract(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 0, "Subtracting 2 to 2 should equal 0")

    def test_multiply(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 4, "Multiplying 2 to 2 should equal 4")

    def test_divide(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 1, "Adding 2 to 2 should equal 4")
