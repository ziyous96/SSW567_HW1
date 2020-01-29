"""
author: Ziyou Shang
These are the test cases for HW01
"""
import math
import unittest
from HW01_Ziyou_Shang import classify_triangle


class TestTriangles(unittest.TestCase):
    """ Test cases for classify_triangle method """

    def test_input(self):
        """ Test if the function can handle invalid input """

        # check for invalid value of length
        self.assertRaises(ValueError, classify_triangle, -1, 2, 3)
        self.assertRaises(ValueError, classify_triangle, -1, 0, 3)
        self.assertRaises(ValueError, classify_triangle, 1, 2, -3.2)
        self.assertRaises(ValueError, classify_triangle, 0, 0, 0)

        # check for string input
        self.assertEqual(classify_triangle("a", 2, 3), "Error")
        self.assertEqual(classify_triangle(1, "b", 3), "Error")
        self.assertEqual(classify_triangle(1, 2, "C"), "Error")
        self.assertEqual(classify_triangle("A", "b", "C"), "Error")

    def test_result(self):
        """ Test if the function returns the correct result """

        # triangles with integer side length
        self.assertEqual(classify_triangle(1, 2, 3), "scalene triangle")
        self.assertEqual(classify_triangle(3, 4, 5), "scalene right triangle")
        self.assertEqual(classify_triangle(4, 5, 3), "scalene right triangle")
        self.assertEqual(classify_triangle(3, 3, 3), "equilateral triangle")
        self.assertEqual(classify_triangle(3, 3, 5), "isosceles triangle")
        self.assertEqual(classify_triangle(3, 5, 3), "isosceles triangle")

        # triangles with float side length
        self.assertEqual(classify_triangle(1, 2.2, 3.3), "scalene triangle")
        self.assertEqual(classify_triangle(3.3, 3.3, 3.3), "equilateral triangle")
        self.assertEqual(classify_triangle(3.3, 3.3, 5), "isosceles triangle")
        self.assertEqual(classify_triangle(3.3, 5, 3.3), "isosceles triangle")
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "isosceles right triangle")
        self.assertEqual(classify_triangle(1.2, math.sqrt((1.2 ** 2) + (2.3 ** 2)), 2.3), "scalene right triangle")
        self.assertEqual(classify_triangle(math.sqrt(5), 1, 2), "scalene right triangle")
        self.assertEqual(classify_triangle(2.23, 2, 1), "scalene triangle")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
