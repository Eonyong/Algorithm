#  runtime error 해결하기
def permu(i, N, arr, stat):
    global answer
    if i == N:
        left, right = arr[:N // 2], arr[N//2:]
        lf, rt = 0, 0
        for s in range(N//2 - 1):
            for e in range(s+1, N//2):
                lf += stat[left[s]][left[e]] + stat[left[e]][left[s]]
                rt += stat[right[s]][right[e]] + stat[right[e]][right[s]]
        if answer > abs(lf - rt):
            answer = abs(lf - rt)

    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            permu(i + 1, N, arr, stat)
            arr[i], arr[j] = arr[j], arr[i]


N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
answer = 100 * (N ** 2)
permu(0, N, list(range(N)), stats)

print(answer)