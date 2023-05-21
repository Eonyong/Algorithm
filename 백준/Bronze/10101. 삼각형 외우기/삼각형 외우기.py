import sys

input = sys.stdin.readline

triangle = sorted([int(input()) for _ in range(3)])
tri_set = set(triangle)

if sum(triangle) == 180:
    if len(tri_set) == 1:
        print('Equilateral')
    elif len(tri_set) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')