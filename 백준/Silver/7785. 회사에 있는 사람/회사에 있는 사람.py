import sys

input = sys.stdin.readline

members = dict()
n = int(input())

for _ in range(n):
    name, state = map(str, input().split())
    if name not in members.keys():
        members[name] = state
    else:
        members[name] = state

for employee in sorted(members.keys(), reverse=True):
    if members[employee] == 'enter':
        print(employee)