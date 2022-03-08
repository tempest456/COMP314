import unittest
from LinearSearch import LinearSearch
from BinarySearch import BinarySearch

class TestLinearSearch(unittest.TestCase):

    def testLinearSearch(self):
        self.assertEqual(LinearSearch([], 3), -1)
        self.assertEqual(LinearSearch([1, 2], 3), -1)
        self.assertEqual(LinearSearch([1, 2, 3, 4], 3), 2)
        self.assertEqual(LinearSearch([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(LinearSearch([1, 2, 3, 4], 3), 2)
        self.assertEqual(LinearSearch([1, 2, 3, 4], 1), 0)
        self.assertEqual(LinearSearch([1, 2, 3, 4], 4), 3)
        
class TestBinarySearch(unittest.TestCase):

    def testBinarySearch(self):
        self.assertEqual(BinarySearch([], 3), -1)
        self.assertEqual(BinarySearch([1, 2], 3), -1)
        self.assertEqual(BinarySearch([1, 2, 3, 4], 3), 2)
        self.assertEqual(BinarySearch([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(BinarySearch([1, 2, 3, 4], 3), 2)
        self.assertEqual(BinarySearch([1, 2, 3, 4], 1), 0)
        self.assertEqual(BinarySearch([1, 2, 3, 4], 4), 3)


if __name__ == '__main__':
    unittest.main()
    
    