def permu(i, N, arr):
    global answer
    if i == N:
        ans = 1
        for work in range(N):
            if not working_day[work][arr[work]]:
                ans = 0
                break
            else:
                ans *= (working_day[work][arr[work]] / 100)
        if answer < ans:
            answer = ans
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            permu(i + 1, N, arr)
            arr[i], arr[j] = arr[j], arr[i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    answer = 0
    working_day = [list(map(int, input().split())) for _ in rangea(N)]
    works = list(range(N))
    permu(0, N, works)
    print(f'#{tc} {answer * 100:.6f}')
