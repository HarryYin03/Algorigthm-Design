import sys
sys.setrecursionlimit(10000)


goods = list(map(int, input().split()))

n = len(goods)
sum_goods = sum(goods)
result = [0] * n
min_diff = float('inf')

def comb(i, left):
 global sum_goods
 global min_diff
 if i == n:
  right = sum_goods - left
  diff = abs(left - right)
  if diff < min_diff:
   min_diff = diff
 else:
  result[i] = 0
  comb(i + 1, left + goods[i])

  result[i] = 1
  comb(i + 1, left)

comb(0, 0)
print(min_diff)