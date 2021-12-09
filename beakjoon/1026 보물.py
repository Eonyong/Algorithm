N = int(input())
answer = 0
A = sorted(list(map(int, input().split())), reverse=True)
B = list(map(int, input().split()))
visited = [True] * N

while A:
    a = A.pop()
    val = 0
    for idx in range(N):
        if visited[idx] and B[idx] > val:
            val = B[idx]
    else:
        visited[B.index(val)] = False
    answer += val * a
print(answer)
