arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[0], x[1]))
for x, y in arr:
    print(f'{x} {y}')