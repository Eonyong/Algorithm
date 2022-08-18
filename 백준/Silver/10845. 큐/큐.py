from collections import deque
import sys

queue = deque()
for _ in range(int(input())):
    commands = sys.stdin.readline().split()
    if len(commands) == 1:
        command = commands.pop()
    elif len(commands) == 2:
        command, val = commands

    if command == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif command == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif command == 'push':
        queue.append(int(val))
