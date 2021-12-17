N, K = map(int, input().split())

up, down = 1, 1
for i in range(1, K + 1):
    up *= (N - i + 1)
    down *= i
print(up // down)
