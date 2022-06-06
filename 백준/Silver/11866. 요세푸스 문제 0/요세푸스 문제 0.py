from collections import deque

n, m = map(int, input().split())
arr = deque(range(1, n + 1))
answer = []
while arr:
    for _ in range(m - 1):
        arr.rotate(-1)
    answer.append(str(arr.popleft()))
answer = ', '.join(answer)
print(f'<{answer}>')