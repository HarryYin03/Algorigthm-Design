N = int(input())
memo = {}

def N_Harvester(n):
 if n in memo:
  return memo[n]
 if n == 0:
  memo[n] = 0
  return memo[n]
 if n == 1: 
  memo[n] = 1
  return memo[n]
 memo[n] = N_Harvester(n-1) + N_Harvester(n-2)
 return memo[n]


print(N_Harvester(N + 1))

 