import sys

input = sys.stdin.readline

boards = []
w = 0
for _ in range(5):
    ls = list(input())
    w = max(w, len(ls))
    boards.append(ls)
answer = ''

for col in range(w):
    for row in range(5):
        if len(boards[row]) > col + 1:
            answer += boards[row][col]
        else:
            continue
print(answer)

