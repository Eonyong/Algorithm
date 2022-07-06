n = int(input())
answer = 0
boards = [[0] * 10 for _ in range(n)]
for idx in range(1, 10):
    boards[0][idx] = 1

for row in range(1, n):
    for col in range(10):
        if not col:
            boards[row][col] += boards[row - 1][col + 1]
        elif col == 9:
            boards[row][col] += boards[row - 1][col - 1]
        else:
            boards[row][col] += boards[row - 1][col - 1] + boards[row - 1][col + 1]
print(sum(boards[-1]) % 1000000000)