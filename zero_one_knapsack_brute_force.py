# Brute Force Approach for 0-1 Knapsack Problem.
def brute_force(cap, w, p):

    assert len(p) == len(w), "The length of p and w must be equal."
    n = len(w)
    maximum_profit = 0
    sol = None
    sol_set = [list(map(int, bin(x)[2:].rjust(n, "0"))) for x in range(2**n)]
    for x in sol_set:
        weight = 0
        profit = 0
        for idx, value in enumerate(x):
            weight += w[idx] * value
            profit += p[idx] * value
        if weight <= cap and profit > maximum_profit:
            maximum_profit = profit
            sol = x
    return sol, maximum_profit

