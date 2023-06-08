import unittest

from sort_algo import insertion_sort, merge_sort

class test_insertionsort(unittest.TestCase):
    
    def test_insertion(self):
        # must pass
        input_val = [3,2,5,6,12,9]
        output_val = [2,3,5,6,9,12]
        self.assertListEqual(insertion_sort(input_val), output_val)

        input_val = [9,8,7,6,5,4,3]
        output_val = [3,4,5,6,7,8,9]
        self.assertListEqual(insertion_sort(input_val), output_val)

        input_val = [7]
        output_val = [7]
        self.assertListEqual(insertion_sort(input_val), output_val)


class test_mergesort(unittest.TestCase):
    def test_merge(self):
        input_val = [3,2,5,6,12,9]
        output_val = [2,3,5,6,9,12]
        self.assertListEqual(merge_sort(input_val,0,len(input_val)-1), output_val)

        input_val = [9,8,7,6,5,4,3]
        output_val = [3,4,5,6,7,8,9]
        self.assertListEqual(merge_sort(input_val, 0, len(input_val)-1), output_val)

        input_val = [7]
        output_val = [7]
        self.assertListEqual(merge_sort(input_val, 0, len(input_val)-1), output_val)

if __name__ == "__main__":
    unittest.main()