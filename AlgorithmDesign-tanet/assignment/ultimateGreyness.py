N = int(input().strip())
colors = []
for i in range(N):
    color = list(map(int, input().split()))
    colors.append(color)

min_diff = float('inf')

def comb(i, total_vividness, total_dullness):
    global min_diff
    if i == N:
        if total_vividness > 0: 
            diff = abs(total_vividness - total_dullness)
            if diff < min_diff:
                min_diff = diff
        return
    comb(i + 1, total_vividness * colors[i][0], total_dullness + colors[i][1])
    comb(i + 1, total_vividness, total_dullness)
comb(0, 1, 0)

print(min_diff)


