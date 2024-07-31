def find_starting_station(n, petrol, distance):
    total_petrol = 0
    total_distance = 0
    tank = 0
    start_station = 0

    for i in range(n):
        total_petrol += petrol[i]
        total_distance += distance[i]
        tank += petrol[i] - distance[i]

        if tank < 0:
            start_station = i + 1
            tank = 0

    if total_petrol < total_distance:
        return -1

    return start_station

# Example input
n = int(input())
petrol = list(map(int, input().split()))
distance = list(map(int, input().split()))

# Find and print the starting gas station
print(find_starting_station(n, petrol, distance))
