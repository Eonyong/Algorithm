import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
union = A & set(B)
for b in B:
    if b in union:
        print(1)
    else:
        print(0)