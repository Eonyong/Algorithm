from collections import deque

for tc in range(1, 11):
    N = int(input())
    arr = deque(list(map(int, input().split())))

    # while arr[-1]:
    #