from simplePriorityQueue import *
N = int(input())
floors = []
for i in range(N):
    floors.append(list(map(int, input().split())))

class state:
    def __init__(self, g):
        self.g = g


pq = Simple_Priority_Queue(lambda x, y: x.g > y.g)
s = state(0)
pq.enqueue(s)
p = []
for i in range(N):
    u = pq.dequeue()
    p.append(u)

    for v in floors[i]:
        a = state(v)
        pq.enqueue(a)

u = pq.dequeue()
p.append(u)


result = 0
for i in range(N + 1):
    result += p[i].g

print(result)