
# knapsack problem using dynamic programming buttom-up approach

def knapsack_dynamic(profits, weights, capacity):

    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0
    
    numberofRows = len(profits) + 1
    dp = [[0 for i in range(capacity+2)] for j in range(numberofRows)]

    for row in range(numberofRows-2, -1, -1):
        for column in range(1, capacity+1):
            profit1 = 0
            profit2 = 0
            if weights[row] <= column:
                profit1 = profits[row] + dp[row+1][column - weights[row]]
            
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    
    return dp[0][capacity]

profit = [50, 30, 70, 40]
weight = [7, 6, 8, 7]
capacity = 16
print(knapsack_dynamic(profit, weight, capacity))


