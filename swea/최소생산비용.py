# 기본적으로 순열을 이용한 방식에 ans를 동적(?)으로 계산하여 값을 구하는 방식
def f(N, i, ans):
    global answer
    if i == N:
        if ans < answer:
            answer = ans
    else:
        # 비교해가면서 값이 커지면 바로 return시켜서 실행시간을 단축
        if ans < answer:
            for j in range(N):
                if not u[j]:
                    u[j] = True
                    ls[i] = arr[j]
                    f(N, i + 1, ans + factory[i][arr[j]])
                    u[j] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(range(N))
    factory = [list(map(int, input().split())) for _ in range(N)]
    u = [False] * N
    ls = [0] * N
    answer = 1e9
    f(N, 0, 0)

    print(f'#{tc} {answer}')