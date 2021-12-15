def direction(s, ls):
    global answer
    if ls[s]:
        for e, m in ls[s]:
            print(s, '-', e - 1)
            answer += m
            direction(e - 1, ls)
    else:
        box.append(answer)

# def direction(s, n, ls):
#     global answer
#     start = s
#     for e in range(n):
#         if ls[start][e]:
#             print(start, e)
#             answer += ls[start][e]
#             direction(e, n, ls)


N = int(input())
arr = [[] * N for _ in range(N)]
box = []
for _ in range(N - 1):
    s, e, m = map(int, input().split())
    arr[s - 1].append([e, m])
answer = 0

direction(0, arr)

print(box)


# direction(0, N, arr)

# if arr[0]:
#     for s, m in arr[0]:
#         answer += m
#         if arr[s]:
#             for s'', m'' in arr[s]:

