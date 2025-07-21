import unittest
from app.calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(20, 8), 12)

if __name__ == '__main__':
    unittest.main()
