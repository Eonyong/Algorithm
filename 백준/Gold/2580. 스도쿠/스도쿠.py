def sudoku(i, n, zeros, boards):
    global answer, flag
    if i == n:
        answer = []
        for board in boards:
            answer.append(board[:])
        else:
            flag = True
    else:
        if not flag:
            r, c = zeros[i]
            row, col = 3 * (r // 3), 3 * (c // 3)
            numbers = set(range(1, 10))
            for idx in range(9):
                numbers -= {boards[r][idx], boards[idx][c], boards[row + idx // 3][col + idx % 3]}
            for num in numbers:
                boards[r][c] = num
                sudoku(i + 1, n, zeros, boards)
                boards[r][c] = 0


global answer, flag
boards, zeros, answer, flag = [], [], [], False
for row in range(9):
    line = list(map(int, input().split()))
    for col in range(9):
        if not line[col]:
            zeros.append([row, col])
    boards.append(line)

z = len(zeros)

sudoku(0, z, zeros, boards)
for ans in answer:
    print(*ans)
