import unittest
import full_name

class test_case(unittest.TestCase):

    def test_full_name_1(self):
        self.assertEqual(full_name.full_name("Chenyu", "Song"), "Chenyu Song")
    
    def test_full_name_2(self):
        self.assertEqual(full_name.full_name("Chenyu123", "Song"), None)

    def test_full_name_3(self):
        self.assertEqual(full_name.full_name("Chenyu", "Song!"), None)

if __name__=="__main__":
    unittest.main(verbosity=2)