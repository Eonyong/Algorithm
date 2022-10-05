import sys
from collections import deque
input = sys.stdin.readline


def Diffusions(virus, boards, visited, N, zero):
    value = 0
    cnt = 0
    for r, c in virus:
        visited[r][c] = 0

    while virus:
        row, col = virus.popleft()
        for j, i in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nj, ni = row + j, col + i
            if 0 <= nj < N and 0 <= ni < N and boards[nj][ni] != 1 and visited[nj][ni] == -1:
                visited[nj][ni] = visited[row][col] + 1
                virus.append([nj, ni])
                if not boards[nj][ni]:
                    cnt += 1
                    value = max(value, visited[nj][ni])

    if cnt == zero:
        return value
    else:
        return float('inf')


def SelectM(i, k, N, M, boards, viruses, arr, zero):
    global answer
    if i == M:
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        answer = min(answer, Diffusions(deque(arr), boards, visited, N, zero))
    else:
        for j in range(k, len(viruses)):
            if viruses[j] not in arr:
                arr.append(viruses[j])
                SelectM(i + 1, j, N, M, boards, viruses, arr, zero)
                arr.pop()


answer = float('inf')
n, m = map(int, input().split())
viruses, boards, zero = [], [], 0
for row in range(n):
    ls = list(map(int, input().split()))
    for col in range(n):
        if ls[col] == 2:
            viruses.append([row, col])
        if not ls[col]:
            zero += 1
    boards.append(ls)
SelectM(0, 0, n, m, boards, viruses, [], zero)
if answer == float('inf'):
    print(-1)
else:
    print(answer)