n, k = map(int, input().split())
coins = reversed([int(input()) for _ in range(n)])
answer = 0
for coin in coins:
    if k // coin:
        answer += k // coin
        k %= coin
    if not k:
        break
print(answer)