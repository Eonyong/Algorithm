def solution(n):
    answer = []
    numbers = 0
    arr = [[0] * i for i in range(1, n + 1)]
    for zero in arr:
        numbers += len(zero)

    row = [1, 0, -1]
    col = [0, 1, -1]
    idx, cnt, ni, nj = 0, 1, -1, 0

    while cnt <= numbers:
        ni += row[idx]
        nj += col[idx]
        if arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            if ni + row[idx] == n or nj + col[idx] == n:
                idx = (idx + 1) % 3

        else:
            ni -= row[idx]
            nj -= col[idx]
            idx = (idx + 1) % 3


    for num in arr:
        for j in num:
            answer.append(j)

    return answer