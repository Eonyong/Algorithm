import sys
from collections import deque

queue = deque()
for _ in range(int(sys.stdin.readline())):
    commands = sys.stdin.readline().split()
    if commands[0] == 'push_front':
        queue.appendleft(int(commands[1]))
    elif commands[0] == 'push_back':
        queue.append(int(commands[1]))
    elif commands[0] == 'pop_front':
        print(queue.popleft()) if queue else print(-1)
    elif commands[0] == 'pop_back':
        print(queue.pop()) if queue else print(-1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        print(0) if queue else print(1)
    elif commands[0] == 'front':
        print(queue[0]) if queue else print(-1)
    elif commands[0] == 'back':
        print(queue[-1]) if queue else print(-1)