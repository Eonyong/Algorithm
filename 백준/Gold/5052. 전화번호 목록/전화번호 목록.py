import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    flag = False
    numnbers = [input().rstrip() for _ in range(n)]
    numnbers.sort(key=lambda x: len(x))
    for s in range(n - 1):
        for e in range(s + 1, n):
            if numnbers[e].startswith(numnbers[s]):
                flag = True
                break
        if flag:
            print("NO")
            break
    else:
        print('YES')