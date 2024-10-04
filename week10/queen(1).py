import copy
q = int(input())

class state():
 def __init__(self, n):
  self.queen = [-1] * n
  self.col = 0

def goal(s):
 if s.col == q:
  return True
 else:
  return False

def conflict(queen, i, c):
 if queen[i] == queen[c] or abs(queen[i]-queen[c]) == abs(i-c):
        return True
 return False

def valid(u):
 for i in range(u.col):
  if conflict(u.queen, i, u.col):
   return False
 return True


def successor(s):
 succ = []
 for i in range(q):
  u = copy.deepcopy(s)
  u.queen[u.col] = i
  if valid(u):
   u.col += 1
   succ.append(u)

 return succ


def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

s = state(q)
queue = []

while not goal(s):
  for x in successor(s):
    queue.append(x)
  s = queue[0]
  del queue[0]

printqueens(s.queen)