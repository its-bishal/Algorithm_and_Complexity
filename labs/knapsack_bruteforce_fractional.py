
# knapsack problem usign brutforce fractional method

def get_strings(n):
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

def not_assigned_weight(strings):
    a = []
    for i, x in enumerate(strings):
        if x == '0':
            a.append(i)
    return a


def knapsack_bruteforce_fractional(p, w, m):
    assert len(p) == len(w), "p and w don't have same no of elements"

    n = len(p)
    bit_strings = list(get_strings(n))

    max_profit = 0
    solution = ''
    for s in bit_strings:
        profit = sum([int(s[i])*p[i] for i in range(n)])
        weight = sum([int(s[i])*w[i] for i in range(n)])

        new_string = not_assigned_weight(bit_strings)
        fraction = 0
        if weight < m:

            for i in new_string:
                remaining = m - weight
                if remaining < w[i]:
                    fraction += (p[i]/w[i])*remaining
                else:
                    fraction += (p[i]/w[i])*w[i]
            profit+= fraction


        if weight <= m and profit > max_profit:
            max_profit = profit
            solution = s

    return max_profit

p = [50, 30, 70, 40]
w = [7, 6, 8, 7]
new = knapsack_bruteforce_fractional(p, w, 20)
print(new)


