n = int(input())
numbers = list(map(int, input().split()))
for idx in range(1, n):
    numbers[idx] = max(numbers[idx], numbers[idx - 1] + numbers[idx])
print(max(numbers))