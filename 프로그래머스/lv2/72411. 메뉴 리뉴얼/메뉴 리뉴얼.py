from collections import defaultdict

def Permutations(i, k, m, n, visited, arr, tot):
    global menus
    if i == m:
        tot.sort()
        tot = ''.join(tot)
        menus[tot] += 1
    else:
        for j in range(k, n):
            if not visited[j]:
                visited[j] = True
                Permutations(i + 1, j, m, n, visited, arr, tot + [arr[j]])
                visited[j] = False

def solution(orders, course):
    global menus
    
    answer = []
    menus = defaultdict(int)
    
    for order in orders:
        n = len(order)
        if n > 2:
            visited = [False for _ in range(n)]
            for idx in range(2, n + 1):
                Permutations(0, 0, idx, n, visited, order, [])
        else:
            menus[order] += 1
            
    tmp = defaultdict(list)
    for k, v in menus.items():
        if v > 1:
            tmp[len(k)].append((k, v))
            
    for c in course:
        if tmp[c]:
            tmp[c].sort(key = lambda x: x[1])
            val = tmp[c][-1][1]
            while tmp[c]:
                k, v = tmp[c].pop()
                if v == val:answer.append(k)
                else:break
    answer.sort()
    return answer