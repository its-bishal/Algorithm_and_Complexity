
# knapsack problem using dynamic programming top down-approach?

def knapsack_dynamic(items, capacity, currentIndex, tempDict):
    dictkey = str(currentIndex) + str(capacity)

    if capacity == 0 or currentIndex <0 or currentIndex >= len(items):
        return 0

    elif dictkey in tempDict:
        return tempDict(currentIndex)
    
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + \
        knapsack_dynamic(items, capacity - items[currentIndex].weight, currentIndex + 1, tempDict)

        profit2 = knapsack_dynamic(items, capacity, currentIndex+1, tempDict)

        tempDict[dictkey] = max(profit1, profit2)
        return tempDict(currentIndex)
    else:
        return 0


profit = [50, 30, 70, 40]
weight = [7, 6, 8, 7]

new = knapsack_dynamic(weight, 20, )