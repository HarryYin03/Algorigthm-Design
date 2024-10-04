# Union-Find (Disjoint Set Union - DSU) Helper functions
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(n, edges):
    # Sort edges by the length of pipes (weight)
    edges.sort(key=lambda x: x[2])
    
    parent = []
    rank = []
    
    # Initialize union-find structure
    for node in range(n):
        parent.append(node)
        rank.append(0)
    
    mst_weight = 0
    mst_edges = 0
    
    # Kruskal's Algorithm to find the minimum spanning tree
    for edge in edges:
        u, v, weight = edge
        
        rootU = find(parent, u)
        rootV = find(parent, v)
        
        # If u and v are not connected, add this edge to the MST
        if rootU != rootV:
            mst_weight += weight
            mst_edges += 1
            union(parent, rank, rootU, rootV)
        
        # If we have already used n-1 edges, we are done
        if mst_edges == n - 1:
            break
    
    return mst_weight

# Input Reading
n, m = map(int, input().split())  # n: number of taps, m: number of pipes
edges = []

# Collecting the input pipes
for _ in range(m):
    u, v, length = map(int, input().split())
    edges.append((u, v, length))

# Run Kruskal's Algorithm to get the minimum possible total length of pipes
result = kruskal(n, edges)

# Output the result
print(result)
