
# knapsack problem usign brutforce 0/1 method

def get_strings(n):
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

def knapsack_bruteforce01(p, w, m):
    assert len(p) == len(w), "p and w don't have same no of elements"

    n = len(p)
    bit_strings = list(get_strings(n))

    max_profit = 0
    solution = ''
    for s in bit_strings:
        profit = sum([int(s[i])*p[i] for i in range(n)])
        weight = sum([int(s[i])*w[i] for i in range(n)])

        if weight <= m and profit > max_profit:
            max_profit = profit
            solution = s

    return max_profit

p = [50, 30, 70, 40]
w = [7, 6, 8, 7]
new = knapsack_bruteforce01(p, w, 20)
print(new)


