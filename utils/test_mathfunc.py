import unittest
import math_func

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(math_func.division(6, 3), 2)
        self.assertRaises(TypeError, math_func.division, 'a', 2)
        

if __name__ == "__main__":
    unittest.main()