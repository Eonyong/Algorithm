import sys

input = sys.stdin.readline
ls = list()

for _ in range(int(input())):
    items = list(map(int, input().split()))
    if len(items) == 2:
        ls.append(items[1])
    else:
        if items[0] == 2:
            try:
                print(ls.pop())
            except:
                print(-1)
        elif items[0] == 3:
            print(len(ls))
        elif items[0] == 4:
            if ls:
                print(0)
            else:
                print(1)
        elif items[0] == 5:
            try:
                print(ls[-1])
            except:
                print(-1)
