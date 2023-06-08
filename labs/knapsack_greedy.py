# kanpsack problem using greedy algorithm approach

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value/weight

def knapsack_greedy(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    usedCapacity  = 0
    totalVal = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalVal += i.value

        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalVal += value

        if usedCapacity == capacity:
            break
        
    print(f'total value obtained {totalVal}')
    return totalVal


item1 = Item(50, 7)
item2 = Item(30, 6)
item3 = Item(70, 6)
item4 = Item(40, 6)
items = [item1, item2, item3, item4]

print(knapsack_greedy(items, 20))
        
