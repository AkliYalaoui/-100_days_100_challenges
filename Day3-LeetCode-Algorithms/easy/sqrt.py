"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
"""
import unittest

## Can be optimised using a binary search 
def square_root(a:int) -> int : 
    if a < 0 : 
        raise Exception("square root is not defined for negative integers")
    if a in [0,1] : 
        return a 
    for b in range((a // 2) + 1) :
        if (b * b == a) or (b*b < a and (b+1)*(b+1) > a) : 
            return b


class TestSquareRootMFunction(unittest.TestCase) : 

    def test_equality(self):
        self.assertEqual(4, square_root(16))
        self.assertEqual(3, square_root(9))
        self.assertEqual(2, square_root(4))
        self.assertEqual(2, square_root(8))
        self.assertEqual(1, square_root(1))
        self.assertEqual(0, square_root(0))

    def test_errors(self):
        with self.assertRaises(Exception) : 
            square_root(-2)


if __name__ == "__main__":
    unittest.main()