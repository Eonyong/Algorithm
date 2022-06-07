for _ in range(int(input())):
    N = int(input())
    arr = [True] * N
    answer = []
    for i in range(2, N):
        if arr[i]:
            answer.append(i)
            for j in range(2 * i, N, i):
                arr[j] = False

    start, end, gap = 0, 0, N
    l = len(answer)
    for s in range(l):
        for e in range(s, l):
            if answer[e] - answer[s] < gap:
                if answer[s] + answer[e] == N:
                    start, end, gap = answer[s], answer[e], answer[e] - answer[s]
                    break
            else:
                break
    print(start, end)
