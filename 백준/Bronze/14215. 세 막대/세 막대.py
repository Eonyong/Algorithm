import sys

input = sys.stdin.readline

triangle = sorted(list(map(int, input().split())))
max_val = triangle.pop()
triangle = sum(triangle)

if triangle > max_val:
    print(triangle + max_val)
else:
    print(triangle * 2 - 1)