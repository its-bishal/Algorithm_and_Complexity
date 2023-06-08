# singly linked list


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in linked list
    def insertion(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == 1:
                self.next = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1

                nextNode = tempnode.next
                tempnode.next = newNode
                newNode.next = nextNode

    # traverse through the list
    def traversion(self):
        if self.head is None:
            print('the list is empty')

        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # search through the list
    def search(self, nodevalue):
        if self.head is None:
            print('the list in empty')

        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    print(node.value)
                    return node.value

                node = node.next
            print('the value doesnot exit')

    # delete a node from the list
    def deletion(self, location):
        if self.head is None:
            print('the list is empty')

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                        node.next = None
                        self.tail = node

            else:
                tempnode = self.head
                count = 0
                while count < location - 1:
                    tempnode = tempnode.next
                    count += 1

                nextnode = tempnode.next
                tempnode.next = nextnode.next


act = Slinkedlist()
act.insertion(1, 1)
act.insertion(3, 1)
act.insertion(2, 0)
act.insertion(0, 2)
print([node.value for node in act])

act.traversion()

act.search(1)
act.deletion(2)
print([node.value for node in act])
