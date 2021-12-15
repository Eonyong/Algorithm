def permu(i, N, arr):
    global answer
    if i == N:
        ans = 0
        times = 0
        for items in arr:
            oper, process = items
            times += process
            ans += (times - oper)
        if answer > ans:
            answer = ans
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            permu(i + 1, N, arr)
            arr[i], arr[j] = arr[j], arr[i]


def solution(jobs):
    answer = 500 * 1000
    jobs = sorted(jobs, key=lambda x: x[0])
    n = len(jobs)
    permu(0, n, jobs)

    return answer


solution([[0, 3], [1, 9], [2, 6]])
