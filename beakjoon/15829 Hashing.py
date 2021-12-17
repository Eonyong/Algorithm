N = int(input())
alpha = list(ord(f) - ord('a') + 1 for f in input())
answer = 0

for num in range(N):
    answer += alpha[num] * 31 ** num

print(answer % 1234567891)