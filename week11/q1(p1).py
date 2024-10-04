class Simple_Priority_Queue:
    def __init__(self, cmp):
        self.list = []
        self.cmp = cmp

    def enqueue(self, item):
        self.list.append(item)
        self.list.sort(key=lambda x: x[1], reverse=True)

    def dequeue(self):
        return self.list.pop()

    def empty(self):
        return len(self.list) == 0

def ucs(graph, start, goal):
    def city_compare(item1, item2):
        return item1[1] < item2[1]  # Compare based on cumulative distance
    
    pq = Simple_Priority_Queue(city_compare)
    pq.enqueue((start, 0, [start]))  # (city_index, cumulative_distance, path)
    visited = set()
    
    while not pq.empty():
        current_city, current_dist, path = pq.dequeue()
        if current_city == goal:
            return current_dist, path  # Return the distance and path when goal is reached
        if current_city in visited:
            continue
        visited.add(current_city)

        for neighbor, distance in graph[current_city]:
            if neighbor not in visited:
                pq.enqueue((neighbor, current_dist + distance, path + [neighbor]))

    return float('inf'), []  # Return infinity and empty path if no path is found

# Manual input setup (replace this section with file reading if needed)
data = """
40
0 5 16
0 27 20
0 28 20
0 35 15
1 22 5
1 26 19
1 39 13
2 16 7
2 21 16
2 32 11
3 10 15
3 24 14
3 25 18
5 10 15
5 16 7
6 13 7
6 21 19
7 29 20
7 32 12
7 36 15
8 28 10
8 29 20
8 32 19
8 35 15
9 21 17
9 32 7
10 16 20
10 19 5
11 20 18
11 37 7
11 38 17
12 18 17
12 32 14
12 38 15
13 35 9
16 28 9
16 30 14
17 23 6
17 38 11
18 22 15
19 27 20
19 28 8
19 30 20
19 34 8
20 36 16
21 33 13
22 37 20
23 29 10
23 30 6
23 31 7
24 33 18
25 35 11
26 37 12
26 39 8
28 37 9
31 35 8
31 38 20

"""

data = data.strip().split('\n')
num_cities = int(data[0])
graph = {i: [] for i in range(num_cities)}

for line in data[1:]:
    u, v, w = map(int, line.split())
    graph[u].append((v, int(w)))
    graph[v].append((u, int(w)))  # Assuming undirected graph for bidirectional paths

goal_city = num_cities - 1  # Assuming you want to go from city 0 to the last city

# Run UCS to find the shortest path from city 0 to the last city
shortest_distance, path = ucs(graph, 0, goal_city)
path_output = "->".join(map(str, path))
print(f"{shortest_distance} ({path_output})")
