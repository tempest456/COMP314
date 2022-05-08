#Greedy Approach for Fractional Knapsack Problem.
def greedy(cap, w, p):

    assert len(p) == len(w), "The length of p and w must be equal."
    
    max_profit = 0
    remaining_capacity = cap
    sol = [0] * len(w)
    
    profit_per_weight = [profit / weight for (profit, weight) in zip(p, w)]
    
    while remaining_capacity != 0:
        max_idx = 0
        for index, value in enumerate(profit_per_weight):
            if value > profit_per_weight[max_idx]:
                max_idx = index
        profit_per_weight[max_idx] = 0
        
        if w[max_idx] <= remaining_capacity:
            sol[max_idx] = 1
            max_profit += p[max_idx]
            remaining_capacity -= w[max_idx]
        else:
            frac = round(remaining_capacity / w[max_idx], 2)
            sol[max_idx] = frac
            max_profit += frac * p[max_idx]
            remaining_capacity = 0
    return sol, max_profit

