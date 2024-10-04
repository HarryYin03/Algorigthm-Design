import copy 


x = input().split()
M = int(x[0])    # number of rows
N = int(x[1])    # number of columns
maze = [[0 for i in range(N)] for j in range(M)]
x = input().split()
sr = int(x[0])
sc = int(x[1])
x = input().split()
dr = int(x[0])
dc = int(x[1])
for i in range(M):
    x = input().split()
    for j in range(N):
        maze[i][j] = -int(x[j])

Adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]



class state:
    def __init__(self, row, column, step):
        self.r = row
        self.c = column
        self.step = step

s = state(sr, sc, 0)
queue = []

def goal(s):
    if s.r == dr and s.c == dc:
        return True
    return False

def valid(r,c):
    if r >= 0 and r < M and c >= 0 and c < N:
        if maze[r][c] == 0:
            return True
    return False

def successor(s):
    succ = []
    for a in Adj:
        u = copy.deepcopy(s)
        u.r += a[0]
        u.c += a[1]
        if valid(u.r, u.c):
            u.step += 1
            maze[u.r][u.c] = u.step
            succ.append(u)
    return succ

while not goal(s):
   for u in successor(s):
        queue.append(u)
   s = queue[0]
   del queue[0]

print(s.step)


