# implements the buckets as linked list, and colliding elements are stored in the list
import slinkedlist

act = slinkedlist.Slinkedlist()
act.insertion(1, 1)
act.insertion(3, 1)
act.insertion(2, 0)
act.insertion(0, 2)
print([node.value for node in act])