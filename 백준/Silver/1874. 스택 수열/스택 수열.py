import sys

input = sys.stdin.readline

n = int(input())
stacks = list(range(n, 0, -1))
tmp = []
answer = []
compares = [int(input()) for _ in range(n)]

pushpop = []

i = 0
while stacks or tmp:
    if compares[i] not in tmp and compares[i] not in answer:
        tmp.append(stacks.pop())
        pushpop.append("+")
    elif compares[i] not in tmp and compares[i] in answer:
        i += 1
    elif compares[i] in tmp:
        answer.append(tmp.pop())
        pushpop.append("-")
        if answer[-1] == compares[i]:
            i += 1

if answer == compares:
    for pp in pushpop:
        print(pp)
else:
    print("NO")
