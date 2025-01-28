"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

"""

import unittest


roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def roman_to_int(r: str) -> int:
    i = 0
    prev = ""
    for l in r :
        if prev == "I" and l in ["V", "X"]:
            i -= 2
        elif prev == "X" and l in ["L", "C"]:
            i -= 20
        elif prev == "C" and l in ["D", "M"]:
            i -= 200
        i += roman_dict[l]
        prev = l
    return i



class TestRomanToInt(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(3, roman_to_int("III"))
        self.assertEqual(58, roman_to_int("LVIII"))
        self.assertEqual(1994, roman_to_int("MCMXCIV"))
        self.assertEqual(27, roman_to_int("XXVII"))
        self.assertEqual(12, roman_to_int("XII"))


if __name__ == "__main__":
    unittest.main()
