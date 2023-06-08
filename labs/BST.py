# binary search tree implementation
from collections import deque

class BinarySearchTree:
    def __init__(self):
        self._size = 0
        self.root = None

    class BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.leftchild = None
            self.rightchild = None
            self.parent = None

    def size(self):
        return self._size
    
    def add(self, key, value):
        new = self.BSTNode(key, value)
        y = None
        x = self.root

        while (x != None):
            y = x
            if (key < x.key):
                x = x.leftchild
            else:
                x = x.rightchild
        
        if y == None:
            self.root = new
        elif new.key < y.key:
            y.leftchild = new
        else:
            y.rightchild = new
        self._size += 1

    def search(self, key):
        x = self.root
        while x!= None:
            if key > x.key:
                x = x.rightchild
            elif key < x.key:
                x = x.leftchild
            else:
                return x.value
            
        return False
    
    def smallest(self):
        x = self.root
        while x.leftchild != None:
            x = x.leftchild
        if x.leftchild == None:
            return x.key, x.value
        
    def largest(self):
        x = self.root
        while x.rightchild != None:
            x = x.rightchild
        if x.rightchild == None:
            return x.key, x.value
        
    def remove(self, key):
        x = self.root
        parent = None

        while x != None and x.key != key:
            parent = x
            if x.key< key:
                x = x.rightchild
            else:
                x = x.leftchild
        
        if x == None:
            return False
        
        if x.leftchild == None or x.rightchild == None:
            y = None
            if x.leftchild == None:
                y = x.rightchild
            else:
                y = x.leftchild
            if parent == None:
                return y
            
            if x == parent.leftchild:
                parent.leftchild = y

            else:
                parent.rightchild = y

            x = None

        else:
            z = None
            temp = x.rightchild
            while temp.leftchild != None:
                z = temp
                temp = temp.leftchild

            if z != None:
                z.leftchild = temp.rightchild
            else:
                x.rightchild = temp.rightchild
            x.key = temp.key
            temp = None
        self._size -= 1

    def inorder_walk(self):
        inorder_list = []
        stack = deque()
        x = self.root
        while stack or x:
            if x:
                stack.append(x)
                x = x.leftchild
            else:
                x = stack.pop()
                inorder_list.append(x.key)
                x = x.rightchild
        return inorder_list
    
    def preorder_walk(self):
        preorder_list = []
        x = self.root
        if x == None:
            return
        stack = deque()
        stack.append(x)
        while stack:
            y = stack.pop()
            preorder_list.append(y.key)
            if y.leftchild:
                stack.append(y.leftchild)
            if y.rightchild:
                stack.append(y.rightchild)
        return preorder_list
    
    def postorder_walk(self):
        postorder_list = []
        x = self.root
        if x == None:
            return
        
        stack = deque()
        stack.append(x)
        out = deque()
        while stack:
            y = stack.pop()
            out.append(y.key)

            if y.rightchild:
                stack.append(y.rightchild)

            if y.leftchild:
                stack.append(y.leftchild)
            
        while out:
            postorder_list.append(out.pop())
        return postorder_list
    
new = BinarySearchTree()
new.add()