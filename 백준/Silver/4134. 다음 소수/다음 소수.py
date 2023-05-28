import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    flag = False
    while True:
        if n < 3:
            print(2)
            break
        for i in range(2, int(n ** .5) + 1):
            if not n % i:
                n += 1
                break
        else:
            flag = True

        if flag:
            print(n)
            break
