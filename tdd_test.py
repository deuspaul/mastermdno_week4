import unittest

from tdd import *

class TwoFerTest(unittest.TestCase):
    #def test_no_name_given(self):
        #self.assertEqual(function("Input"), "Expected Output")

    def test_check_string_length(self)    :
        self.assertEqual(check_length("Hello"), 5)
        self.assertEqual(check_length("Hello World"), 11)

    def test_check_empty_value(self):
        self.assertEqual(check_length(), 0)
        self.assertEqual(check_length(""), 0)

    def test_check_product(self):
        self.assertEqual(check_product([1,1,5]), 5)

    def test_check_multiply_by_zero(self):
        self.assertEqual(check_product([10, 0]), 0)
        self.assertEqual(check_product([0, 10]), 0)
        self.assertEqual(check_product([10, 1, 5, 0, 948, 2, 10]), 0)

    def test_check_product_negative_values(self):
        self.assertEqual(check_product([-1, 1, 5]), -5)
        self.assertEqual(check_product(), 0)

    def test_odd_string_return(self):
        self.assertEqual(odd_string("Hello There You"), "Hel hr o")
        self.assertEqual(odd_string("Yes"), "Ye")
        self.assertEqual(odd_string(""), "")


if __name__ == "__main__":
    unittest.main()