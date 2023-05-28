import sys

input = sys.stdin.readline

dictionaries = dict()
n, m = map(int, input().split())
for _ in range(n):
    name = input().rstrip()
    if name not in dictionaries.keys():
        dictionaries[name] = 1
    else:
        dictionaries[name] += 1


dictionaries = sorted(dictionaries.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for name, cnt in dictionaries:
    if len(name) >= m:
        print(name)