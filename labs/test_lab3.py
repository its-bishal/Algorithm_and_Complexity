import unittest
from BST import BinarySearchTree

class BSTTestCase(unittest.TestCase):

    def setUp(self):
        """
        Executed before each test method.
        Before each test method, create a BST with some fixed key-values. 
        """
        self.bst = BinarySearchTree()
        self.bst.add(10, 9)
        self.bst.add(52, 16)
        self.bst.add(5, 40)
        self.bst.add(8, 25)
        self.bst.add(1, 2)
        self.bst.add(40, 20)
        self.bst.add(30, 80)
        self.bst.add(45, 75)
    
    def test_add(self):
        """
        tests for add
        """
        # Create an instance of BinarySearchTree
        bsTree = BinarySearchTree()

        # bsTree must be empty
        self.assertEqual(bsTree.size(), 0)
        
        # Add a key-value pair
        bsTree.add(15, "Value for 15")
        # Size of bsTree must be 1
        self.assertEqual(bsTree.size(), 1)

        # Add another key-value pair
        bsTree.add(10, "Value for 10")
        # Size of bsTree must be 2
        self.assertEqual(bsTree.size(), 2)

        # The added keys must exist.
        self.assertEqual(bsTree.search(10), 8)
        self.assertEqual(bsTree.search(15), 5)

    def test_inorder(self):
        """
        tests for inorder_walk
        """
        actual_output = self.bst.inorder_walk()
        expected_output = [1, 5, 8, 10, 30, 40, 45, 52]

        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, 33)
        # Inorder traversal must return a different sequence
        self.assertListEqual(self.bst.inorder_walk(), [1, 5, 8, 10, 25, 30, 40, 45, 52])

    def test_postorder(self):
        """
        tests for postorder_walk
        """
        actual_output = self.bst.postorder_walk()
        expected_output = [1, 8, 5, 30, 45, 40, 52, 10]
        
        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, 33)
        # Postorder traversal must return a different sequence
        self.assertListEqual(self.bst.postorder_walk(), [1, 8, 5, 25, 30, 45, 40, 52, 10])

    def test_preorder(self):
        """
        tests for preorder_walk
        """
        self.assertListEqual(self.bst.preorder_walk(), [10, 5, 1, 8, 52, 40, 30, 45])

        # Add one node
        self.bst.add(25, 33)
        # Preorder traversal must return a different sequence
        self.assertListEqual(self.bst.preorder_walk(), [10, 5, 1, 8, 52, 40, 30, 25, 45])
    
    def test_search(self):
        """
        tests for search
        """
        actual_output = self.bst.search(40)
        expected_output = 20
        self.assertEqual(actual_output, expected_output)
    
        self.assertFalse(self.bst.search(90))

        self.bst.add(90, 100)
        self.assertEqual(self.bst.search(90), 100)

    def test_remove(self):
        """
        tests for remove
        """
        self.bst.remove(40)
        
        self.assertEqual(self.bst.size(), 7)
        self.assertListEqual(self.bst.inorder_walk(), [1, 5, 8, 10, 30, 45, 52])
        self.assertListEqual(self.bst.preorder_walk(), [10, 5, 1, 8, 52, 30, 45])

    def test_smallest(self):
        """
        tests for smallest
        """
        self.assertTupleEqual(self.bst.smallest(), (1, 2))

        # Add some nodes
        self.bst.add(6, 66)
        self.bst.add(4, 44)
        self.bst.add(0, 0)
        self.bst.add(32, 39)

        # Now the smallest key is 0.
        self.assertTupleEqual(self.bst.smallest(), (0, 0))

    def test_largest(self):
        """
        tests for largest
        """
        self.assertTupleEqual(self.bst.largest(), (52, 16))

        # Add some nodes
        self.bst.add(6, 66)
        self.bst.add(54, 45)
        self.bst.add(0, 0)
        self.bst.add(32, 39)

        # Now the largest key is 54
        self.assertTupleEqual(self.bst.largest(), (54, 45))

if __name__ == "__main__":
    unittest.main()    