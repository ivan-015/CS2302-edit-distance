# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 7
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 12/06/2018
# The purpose of this program is to test
# edit_distance.py
import unittest
import edit_distance


class TestEditDistance(unittest.TestCase):

    # Function to test edge cases
    def test_edge(self):
        # Test with s1 empty, s2 non empty, should return length of s2
        self.assertEqual(edit_distance.compute_edit_distance("", "camera"), 6)
        # Test with both empty strings, should return 0
        self.assertEqual(edit_distance.compute_edit_distance("", ""), 0)
        # Test with non empty s1, and empty s2, should return length of s1
        self.assertEqual(edit_distance.compute_edit_distance("plane", ""), 5)
        # Test with identical strings, should return 0
        self.assertEqual(edit_distance.compute_edit_distance("flicker", "flicker"), 0)

    # Function for regular string testing
    def test_regular(self):
        self.assertEqual(edit_distance.compute_edit_distance("miners", "monkey"), 4)
        self.assertEqual(edit_distance.compute_edit_distance("potato", "intricate"), 6)
        self.assertEqual(edit_distance.compute_edit_distance("telephone", "television"), 5)
        self.assertEqual(edit_distance.compute_edit_distance("computer", "vehicle"), 7)
        self.assertEqual(edit_distance.compute_edit_distance("vihuela", "refrigerator"), 10)


if __name__ == "__main__":
    unittest.main()
