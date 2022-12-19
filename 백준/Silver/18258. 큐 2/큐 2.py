import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    commands = input().split()
    if commands[0] == 'push':
        queue.append(int(commands[1]))
    elif commands[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif commands[0] == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        print(1) if not queue else print(0)
    elif commands[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
