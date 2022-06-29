def makeOne(n, cnt):
    global answer
    if n == 1:
        answer = min(cnt, answer)
    elif n > 1 and answer > cnt:
        if not n % 3:
            makeOne(n // 3, cnt + 1)
        if not n % 2:
            makeOne(n // 2, cnt + 1)
        makeOne(n - 1, cnt + 1)


global answer
answer = float('inf')
n = int(input())
makeOne(n, 0)
print(answer)
