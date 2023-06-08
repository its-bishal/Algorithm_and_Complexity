

class BinarySearchTree:

    class Node:

        def __init__(self, value, parent = None):
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None


    def __init__(self, iterable=None):
        self._root = None
        if iterable is not None:
            for element in iterable:
                self.add(element)


    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)


    def __contains__(self,item):
        return self._search(self._root, item)


    def __len__(self):
        return self._count(self._root)
    

    def search(self, value):
        node = self._search(self._root, value)
        if node is None:
            return None
        return node.value
    
    def _search(self, node, value):
        if node is None:
            return None
        
        if node.value == value:
            return node
        
        if value < node.value:
            return self._search(node.left, value)
        
        else:
            return self._search(node.right, value)


    def add(self, element):
        if self._root is None:
            self._root = self.Node(element)
            return
        
        self._add(self._root, element)


    def _add(self, node, element):
        if element <= node.value:
            if node.left is None:
                node.left = self.Node(element, node)

            else:
                self._add(node.left, element)

        else:
            if node.right is None:
                node.right = self.Node(element, node)

            else:
                self._add(node.right, element)

    
    def remove(self, element):
        node = self._search(self._root, element)
        if node is None:
            raise ValueError('element not found')
        
        parent = node.parent
        if node.left is None and node.right is None:
            if parent is not None:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

            else:
                self._root = None

        elif node.left is None:
                if parent is None:
                    self._root = node.right
                elif parent.left is node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                node.right.parent = parent

        elif node.right is None:
            if parent is None:
                if parent is None:
                    self._root = node.left
                elif parent.left is node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                node.left.parent = parent

        else:
            if parent is None:
                newNode = self._largest(node)
                newNode.parent.right = None
                newNode.parent = None
                newNode.left = node.left
                newNode.right = node.right
                self._root = newNode

            elif parent.left is node:
                newNode = self._largest(node)
                newNode.parent.right = None
                newNode.parent = parent
                newNode.left = node.left
                newNode.right = node.right

            else:
                newNode = self._smallest(node)
                newNode.parent.left = None
                newNode.parent = parent
                newNode.left = node.left
                newNode.right = node.right


    def largest(self):
        if self._root is None:
            raise ValueError('empty BST')
        
        return self._largest(self._root).value


    def _largest(self, node):
        while node.right is not None:
            node = node.right
        return node
    

    def smallest(self):
        if self._root is None:
            raise ValueError('empty BST')
        
        return self._smallest(self._root).value


    def _smallest(self, node):
        while node.left is not None:
            node = node.left

        return node


    def inorder_walk(self, node):
        if node is None:
            return    
        self.inorder_walk(self, node.right)
        print (node.value)
        self.inorder_walk(self, node.left)


    def postorder_walk(self, node):
        if node is None:
            return
        self.postorder_walk(self, node.left)
        print(node.value)
        self.postorder_walk(self, node.right)

        
    def preorder_walk(self, node):
        if node is None:
            return
        print(node.value)
        self.preorder_walk(self, node.left)
        self.preorder_walk(self, node.right)



newvalue = BinarySearchTree()
newvalue.add(4)
newvalue.add(2)
newvalue.add(6)
newvalue.add(1)
newvalue.add(3)
newvalue.add(5)

newvalue.largest()
newvalue.smallest()

# newvalue.inorder_walk(2)
# newvalue.postorder_walk(2)
# newvalue.preorder_walk(2)

newvalue.remove(3)
print(newvalue)