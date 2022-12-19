import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

numbers = deque(range(1, n + 1))
answer = 0

for q in list(map(int, input().split())):
    if numbers[0] == q:
        numbers.popleft()
    else:
        idx = numbers.index(q)
        if idx > len(numbers) - idx:
            numbers.rotate(len(numbers) - idx)
            answer += len(numbers) - idx
        else:
            numbers.rotate(-idx)
            answer += idx

        numbers.popleft()
print(answer)