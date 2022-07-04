n, m = map(int, input().split())
cnt = 0
max_val = max(n, m) * 2 + 1
visited = [False for _ in range(max_val)]
visited[n], histories = True, [n]
if n == m:
    print(0)
else:
    while histories:
        cnt += 1
        next_history = []
        for history in histories:
            for num in [history + 1, history - 1, history * 2]:
                if 0 <= num < max_val and not visited[num]:
                    visited[num] = True
                    next_history.append(num)
        if visited[m]:
            break
        else:
            histories = next_history[:]
    print(cnt)
