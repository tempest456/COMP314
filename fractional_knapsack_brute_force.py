# Brute Force Approach for Fractional Knapsack Problem.
def brute_force(cap, w, p):

    assert len(p) == len(w), "The length of p and w must be equal."
    
    n = len(w)
    max_profit = 0
    max_weight = 0
    sol = None
    sol_set = [list(map(int, bin(x)[2:].rjust(n, "0"))) for x in range(2**n)]
    
    for entry in sol_set:
        weight = 0
        profit = 0
        for idx, value in enumerate(entry):
            weight += w[idx] * value
            profit += p[idx] * value
        if weight <= cap and profit > max_profit:
            max_profit = profit
            sol = entry
            max_weight = weight
    
    remaining_capacity = cap - max_weight
    
    max_fractional_profit = 0
    for idx, weight in enumerate(w):
        if remaining_capacity > 0 and sol[idx] == 0:
            ratio = round(remaining_capacity / weight, 2)
            fractional_profit = ratio * p[idx]
            if fractional_profit > max_fractional_profit:
                max_fractional_profit = fractional_profit
                sol[idx] = ratio
    return sol, max_profit + max_fractional_profit

