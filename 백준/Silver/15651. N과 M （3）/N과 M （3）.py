def prune(i, n, arr, ls, m):
    if len(arr) == m:
        print(*arr)
    else:
        for j in range(n):
            arr.append(ls[j])
            prune(i + 1, n, arr, ls, m)
            arr.pop()


n, m = map(int, input().split())

prune(0, n, [], range(1, n + 1), m)
