import sys;
sys.setrecursionlimit(10000)

def f(x):
    if x == 0:
        print("done")
        return
    else:
        y = [(x-1)+1]
        print(y)
        return y

x = int(input())
print(f(x))