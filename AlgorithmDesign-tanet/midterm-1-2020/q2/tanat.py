# Input
N = int(input())
Petrol = list(map(int, input().split()))
Distance = list(map(int, input().split()))

def circle(Petrol, Distance):
    start = 1
    dept = 0
    extra = 0
    for i in range(len(Petrol)):
        extra += Petrol[i] - Distance[i]
        if extra < 0:
            dept += abs(Petrol[i] - Distance[i])
            extra = 0
            start += 1
    if (extra >= dept):
        return start
    else:
        return -1


print(circle(Petrol, Distance))



