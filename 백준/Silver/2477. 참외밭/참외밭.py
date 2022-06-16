n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

x, y, small = 0, 0, 0

for idx in range(6):
    a, b, c = idx, (idx + 1) % 6, (idx + 2) % 6
    if arr[a][0] == arr[c][0] == 3:
        if arr[b][0] == 1:
            small = arr[b][1] * arr[c][1]
        elif arr[b][0] == 2:
            small = arr[b][1] * arr[a][1]
    elif arr[a][0] == arr[c][0] == 4:
        if arr[b][0] == 1:
            small = arr[b][1] * arr[a][1]
        elif arr[b][0] == 2:
            small = arr[b][1] * arr[c][1]
    if arr[a][0] == 3 or arr[a][0] == 4:
        x = max(x, arr[a][1])
    else:
        y = max(y, arr[a][1])
print((x * y - small) * n)
