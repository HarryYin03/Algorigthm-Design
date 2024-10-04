V, E = map(int, input().split())
edges = []

for i in range(E):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()

from disjointsets3 import DisjointSets

djs = DisjointSets(V)
mst_weight = 0

for w, a, b in edges:
    if djs.findset(a) != djs.findset(b):
        djs.union(a,b)
        mst_weight += w

print(mst_weight)
