import sys

input = sys.stdin.readline

while True:
    try:
        n, k = map(int, input().split())
        answer = n
        while n:
            div, mod = divmod(n, k)
            answer += div
            if not div:
                break
            n = div + mod
        print(answer)
    except:
        break
