import sys

input = sys.stdin.readline

answer = []
name = input().rstrip()
n = len(name)

for idx in range(n):
    answer.append(name[idx:])
answer.sort()

for ans in answer:
    print(ans)