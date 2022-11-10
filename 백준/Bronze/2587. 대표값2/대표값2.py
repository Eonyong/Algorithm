import sys
input = sys.stdin.readline

numbers = sorted([int(input()) for _ in range(5)])
print(sum(numbers) // 5)
print(numbers[5 // 2])