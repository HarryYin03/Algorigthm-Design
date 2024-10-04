rows, cols = map(int, input().split())

image = []

for i in range(rows):
    image.append(list(map(int, input().split())))

def is_valid(i, j):
    return 0 <= i < rows and 0 <= j < cols and image[i][j] == 1

def dfs(i, j):
    if not is_valid(i, j):
        return 0
    image[i][j] = -1
    size = 1
    size += dfs(i - 1, j)
    size += dfs(i + 1, j)
    size += dfs(i, j - 1)
    size += dfs(i, j + 1)
    return size

largest_cloud_size = 0

for i in range(rows):
    for j in range(cols):
        if is_valid(i, j):
            cloud_size = dfs(i, j)
            largest_cloud_size = max(largest_cloud_size, cloud_size)

print(largest_cloud_size)
