from collections import deque
 
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    dic = dict()
    deq = deque([[N, 0]])
    while deq:
        n, m = deq.popleft()
        if n == M:
            print(f'#{tc} {m}')
            break
        else:
            if 0 < n <= 1e6 and n not in dic.keys():
                    dic[n] = 1 + m
                    for i in [n + 1, n - 1, n * 2, n - 10]:
                        deq.append([i, m + 1])