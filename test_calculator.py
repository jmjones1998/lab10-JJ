#https://github.com/jmjones1998/lab10-JJ.git
#Partner 1: Julia Jones
#Partner 2: Julia Jones

import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(12,8),20)
        self.assertEqual(add(0,0),0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,2), -1)
        self.assertEqual(subtract(5,2),3)
        self.assertEqual(subtract(0,    0), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(5,5),25)
        self.assertEqual(mul(-4,2),-8)
        self.assertEqual(mul(3,2),6)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(6,2),3)
        self.assertEqual(div(4,2),2)
        self.assertAlmostEqual(div(7,3),7/3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(8,2),3)
        self.assertAlmostEqual(logarithm(27,3),3)
        self.assertAlmostEqual(logarithm(100,10),2)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        from calculator import logarithm
        with self.assertRaises(ValueError):
            logarithm(0,10)

    def test_hypotenuse(self): # 3 assertions
        from calculator import hypotenuse
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(8,15),17)

    def test_sqrt(self): # 3 assertions
        from calculator import square_root
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2.25),1.5)

        with self.assertRaises(ValueError):
            square_root(-25)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()