def solution(elements):
    n = len(elements)
    Set = set()
    ls = [0 for _ in range(n)]
    for l in range(n):
        for idx in range(n):
            ls[idx] += elements[(idx + l) % n]
            Set.add(ls[idx])
    
    return len(list(Set))