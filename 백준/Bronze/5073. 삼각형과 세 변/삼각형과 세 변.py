import sys

input = sys.stdin.readline

while True:
    
    triangle = sorted(list(map(int, input().split())))
    
    if triangle == [0, 0, 0]:
        break
    
    if sum(triangle[:2]) > triangle[2]:
        if triangle[0] == triangle[1] != triangle[2] or triangle[1] == triangle[2] != triangle[0]:
            print('Isosceles')
        elif triangle[0] == triangle[1] == triangle[2]:
            print('Equilateral')
        else:
            print('Scalene')
    else:
        print('Invalid')