from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    scores = defaultdict(int)
    for idx in range(len(name)):
        scores[name[idx]] = yearning[idx]
    
    for p in photo:
        n = len(p)
        tmp = 0
        for idx in range(n):
            if p[idx] in name:
                tmp += scores[p[idx]]
        answer.append(tmp)
        
    return answer