from collections import deque
import sys

stacks = deque()
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        stacks.append(int(command[1]))
    else:
        if command[0] == 'pop':
            if stacks:
                print(stacks.pop())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(stacks))
        elif command[0] == 'empty':
            if not stacks:
                print(1)
            else:
                print(0)
        elif command[0] == 'top':
            if stacks:
                print(stacks[-1])
            else:
                print(-1)