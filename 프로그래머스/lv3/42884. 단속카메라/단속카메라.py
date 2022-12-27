def solution(routes):
    answer = 0
    n = len(routes)
    routes.sort(key = lambda x: x[1])
    routes = [sorted(route) for route in routes]

    ls = [0 for _ in range(n)]
    for idx in range(n):
        s, e = routes[idx]
        if not ls[idx]:
            answer += 1
            for iidx in range(idx, n):
                x, y = routes[iidx]
                if x <= e:
                    ls[iidx] = answer
                else:
                    break
    return answer