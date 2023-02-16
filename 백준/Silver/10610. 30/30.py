import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)


def BigNumber(i, n, val, visited, numbers):
    global answer
    if i == n:
        if not val % 30:
            answer = max(answer, val)
            return
    else:
        for j in range(n):
            if not visited[j]:
                visited[j] = True
                val = val * 10 + numbers[j]
                BigNumber(i + 1, n, val, visited, numbers)
                visited[j] = False
                val //= 10


answer = 0
numbers = list(map(int, list(input().rstrip())))
numbers.sort(reverse=True)
n = len(numbers)

sumval, z_flag = 0, False
for number in numbers:
    if not number:
        z_flag = True
    sumval += number

if not sumval % 3 and z_flag:
    for idx in range(n):
        answer = answer * 10 + numbers[idx]
else:
    answer = -1
print(answer)
