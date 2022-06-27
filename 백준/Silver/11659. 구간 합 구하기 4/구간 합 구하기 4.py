n, m = map(int, input().split())
numbers = list(map(int, input().split()))
for idx in range(1, n):
    numbers[idx] += numbers[idx - 1]
numbers = [0] + numbers[:]
for _ in range(m):
    s, e = map(int, input().split())
    print(numbers[e] - numbers[s - 1])