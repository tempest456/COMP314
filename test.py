import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort

class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        input = [3, 2, 1, 5, 4]
        output = [1, 2, 3, 4, 5]

        insertion_sort(input)

        self.assertListEqual(input, output)

        input = [1, 2, 3, 4, 5]

        insertion_sort(input)
        self.assertListEqual(input, output)

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        input = [3, 2, 1, 5, 4]
        output = [1, 2, 3, 4, 5]

        merge_sort(input)
        self.assertListEqual(input, output)

        input = [1, 2, 3, 4, 5]

        merge_sort(input)
        self.assertListEqual(input, output)

if __name__ == '__main__':
    unittest.main()

