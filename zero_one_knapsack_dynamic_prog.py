# Dynamic Programming approach for 0-1 Knapsack problem.

def dynamic_prog(cap, w, p):

    assert len(p) == len(w), "The length of p and w must be equal."
    n = len(w)
    knapsack_table = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if j - w[i - 1] < 0:
                knapsack_table[i][j] = knapsack_table[i - 1][j]
            else:
                knapsack_table[i][j] = max(
                    knapsack_table[i - 1][j],
                    knapsack_table[i - 1][j - w[i - 1]] + p[i - 1],
                )
 
 
    max_profit = knapsack_table[n][cap]
    row = n
    col = cap
    sol = [0] * n
    
    # Traversing the knapsack_table from bottom to top to find the solution set.
    while row > 0 and col > 0:
        if knapsack_table[row][col] != knapsack_table[row - 1][col]:
            sol[row - 1] = 1
            col -= w[n - 1]
        row -= 1
        
    return sol, max_profit

