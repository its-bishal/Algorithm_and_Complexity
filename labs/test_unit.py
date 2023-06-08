import unittest

from search_algo import linear_search, binary_search

class test_linearsearch(unittest.TestCase):
    values = [3,6,1,4,8,21,34,13,56,87]
    def test_linear(self):
        # must pass case
        self.assertEqual(linear_search(values=self.values, target=4), 3)
        self.assertEqual(linear_search(values=self.values, target=8), 4)
        self.assertEqual(linear_search(values=self.values, target=56), 8)
        self.assertNotEqual(linear_search(values=self.values, target=91), 7)

        # must fail case
        self.assertEqual(linear_search(values=self.values, target=87), 4)

class test_binarysearch(unittest.TestCase):
    values = [1,2,3,5,7,11,13,17,19,23,29,31,37]
    length = len(values)

    def test_binary(self):
        # must pass case
        self.assertEqual(binary_search(values=self.values, start=0, end=self.length, target=5), 4)
        self.assertEqual(binary_search(values=self.values, start=0, end=self.length, target=13), 6)
        self.assertEqual(binary_search(values=self.values, start=0, end=self.length, target=23), 9)
        self.assertNotEqual(binary_search(values=self.values, start=0, end=self.length, target=41), 7)

        # must fail case
        self.assertEqual(binary_search(values=self.values, start=0, end=self.length, target=93),11)


if __name__ == "__main__":
    unittest.main()