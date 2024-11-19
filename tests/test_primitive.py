import unittest
from primitive_operations import is_prime, sum_of_digits, truncate_float, is_even, is_palindrome_number

class TestPrimitiveOperations(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(17))

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(9876), 30)

    def test_truncate_float(self):
        self.assertAlmostEqual(truncate_float(3.14159), 3.14, places=2)
        self.assertAlmostEqual(truncate_float(0.987654), 0.98, places=2)
        self.assertAlmostEqual(truncate_float(10.0), 10.0, places=2)

class TestBooleanOperations(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-3))

    def test_is_palindrome_number(self):
        self.assertTrue(is_palindrome_number(121))
        self.assertFalse(is_palindrome_number(123))
        self.assertTrue(is_palindrome_number(0))
        self.assertTrue(is_palindrome_number(1221))

if __name__ == '__main__':
    unittest.main()
