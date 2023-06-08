
import unittest

from knapsack_bruteforce_01 import knapsack_bruteforce01
from knapsack_bruteforce_fractional import knapsack_bruteforce_fractional
from knapsack_greedy import knapsack_greedy, Item
from knapsack_dynamic import knapsack_dynamic

class test_knapsack(unittest.TestCase):

    def test_bruteforce01(self):
        profit = [50, 30, 70, 40]
        weight = [7, 6, 8, 7]

        input_val = knapsack_bruteforce01(profit, weight, 20)
        output_val = 120
        
        self.assertEqual(input_val, output_val)

    
    def test_bruteforce_fractional(self):
        profit = [50, 30, 70, 40]
        weight = [7, 6, 8, 7]

        input_val = knapsack_bruteforce_fractional(profit, weight, 20)
        output_val = 120

        self.assertEqual(input_val, output_val)

    def test_greedy(self):
        item1 = Item(50, 7)
        item2 = Item(30, 6)
        item3 = Item(70, 6)
        item4 = Item(40, 6)
        items = [item1, item2, item3, item4]

        input_val = knapsack_greedy(items, 20)
        output_val = 165.0

        self.assertEqual(input_val, output_val)

    def test_dynamic(self):
        profit = [50, 30, 70, 40]
        weight = [7, 6, 8, 7]
        capacity = 16

        input_val = knapsack_dynamic(profit, weight, capacity)
        output_val = 120

        self.assertEqual(input_val, output_val)

if __name__ == "__main__":
    unittest.main()