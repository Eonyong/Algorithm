def SandWind(row, col, arr, N, role, answer):


    sand = arr[row][col]
    for y, x, percent in direction[role]:
        if 0 <= row + y < N and 0 <= col + x < N:
            if percent == 1:
                arr[row + y][col + x] += arr[row][col]
                arr[row][col] = 0
            else:
                arr[row + y][col + x] += int(sand * percent)
                arr[row][col] -= int(sand * percent)
        else:
            if percent == 1:
                answer += arr[row][col]
                arr[row][col] = 0
            else:
                arr[row][col] -= int(sand * percent)
                answer += int(sand * percent)

    return arr, answer


N = int(input())
tonado = [list(map(int, input().split())) for _ in range(N)]

answer = 0

row, col = N // 2, N // 2
cnt = 0
flag = 1
while flag:
    cnt += 1
    for _ in range(cnt):
        col -= 1
        tonado, answer = SandWind(row, col, tonado, N, 1, answer)
        if not row and not col:
            flag = 0
            break
    if not flag:
        break
    for _ in range(cnt):
        row += 1
        tonado, answer = SandWind(row, col, tonado, N, 2, answer)

    cnt += 1
    for _ in range(cnt):
        col += 1
        tonado, answer = SandWind(row, col, tonado, N, 3, answer)

    for _ in range(cnt):
        row -= 1
        tonado, answer = SandWind(row, col, tonado, N, 4, answer)

print(answer)