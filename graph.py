# Python program to print all the cycles in an undirected graph.
N = 1000
 
# variables to be used in both functions
graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]
 
 
# Function to mark the vertex with different colors for different cycles.
def dfs_cycle(u, p, color: list,
              mark: list, par: list):
    global cyclenumber
 
    # Completely visited vertex.
    if color[u] == 2:
        return
 
    """ Seen vertex, but was not
        completely visited thus cycle is detected.
        Backtrack based on parents to
        find the complete cycle. """
    if color[u] == 1:
        cyclenumber += 1
        cur = p
        mark[cur] = cyclenumber
 
        # Backtrack the vertex which are in the currently found cycle.
        while cur != u:
            cur = par[cur]
            mark[cur] = cyclenumber
 
        return
 
    par[u] = p
 
    # Partially visited.
    color[u] = 1
 
    # Simple dfs on graph
    for v in graph[u]:
 
        # If it has not been visited previously
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, mark, par)
 
    # Completely visited.
    color[u] = 2
 
# Function to add edges to the graph.
def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)
 
# Function to print all the cycles in the graph.
def largest_cycle(edges, mark: list):
 
    for i in range(1, edges + 1):
        if mark[i] != 0:
            cycles[mark[i]].append(i)
    
    for i in range(1, cyclenumber + 1):
 
        # Print the i-th cycle
        print("Cycle Number %d:" % i, end = " ")
        for x in cycles[i]:
            print(x, end = " ")
        print()   

# Function to print the largest cycle.
def print_largest_cycle():
    print("The largest cycle is:")
    max = 0
    count = -1
    index = 0
    for i in cycles:
        count += 1
        length = len(i)
        if length>max:
            max = length
            index = count
    print(cycles[index])


if __name__ == "__main__":
 
    # add edges
    addEdge(1, 2)
    addEdge(2, 3)
    addEdge(3, 4)
    addEdge(4, 5)
    addEdge(5, 6)
    addEdge(3, 7)
    addEdge(6, 10)
    addEdge(7, 8)
    addEdge(8, 9)
    addEdge(9, 10)
    addEdge(10, 11)
    addEdge(11, 12)
    addEdge(11, 13)
    addEdge(12, 13)
 
    # Arrays required to color the graph, store the parent of node
    color = [0] * N
    par = [0] * N
 
    # Mark with unique numbers
    mark = [0] * N
 
    # Stores the numbers of cycle
    cyclenumber = 0
    edges = 13
 
    # Call DFS to mark the cycles
    dfs_cycle(1, 0, color, mark, par)
 
    # Function to print the cycles
    largest_cycle(edges, mark)
    
    # Function to print the largest cycle
    print_largest_cycle()
 
