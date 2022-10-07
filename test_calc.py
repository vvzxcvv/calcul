import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(4, 2), 6)


    def test_subtract(self):
        self.assertEqual(calc.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(calc.divide(20, 10), 2)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()