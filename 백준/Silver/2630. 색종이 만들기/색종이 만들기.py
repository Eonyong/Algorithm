import sys

input = sys.stdin.readline


def ColorScript(r, c, m, boards, visited):
    global answer
    first = boards[r][c]
    if m == 1:
        answer[first] += 1
    else:
        for row in range(r, r + m):
            for col in range(c, c + m):
                if boards[row][col] != first:
                    middle = m // 2
                    for j, i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
                        ColorScript(r + j * middle, c + i * middle, middle, boards, visited)
                    return
        answer[first] += 1
        return


n = int(input())
answer = [0, 0]
boards = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
ColorScript(0, 0, n, boards, visited)

for ans in answer:
    print(ans)
