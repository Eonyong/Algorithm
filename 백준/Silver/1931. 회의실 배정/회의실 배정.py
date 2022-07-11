import sys

n = int(sys.stdin.readline())
timeTables = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
timeTables.sort(key=lambda x: (x[1], x[0]))
classTime, cnt = 0, 0
for start, end in timeTables:
    if start >= classTime:
        cnt += 1
        classTime = end
print(cnt)