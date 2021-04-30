import unittest
import calc_average

class test_case(unittest.TestCase):

    def test_average_1(self):
        self.assertEqual(calc_average.calc_average([1,3,5,7,9]),5)
    
    def test_average_2(self):
        self.assertEqual(calc_average.calc_average([1,2,3,4,"i"]), None)

    def test_average_3(self):
        self.assertEqual(calc_average.calc_average([]), None)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)