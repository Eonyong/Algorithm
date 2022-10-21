from collections import defaultdict

def solution(X, Y):
    answer = ''
    x, y = defaultdict(int), defaultdict(int)
    for i in range(len(X)):
        x[X[i]] += 1
    for i in range(len(Y)):
        y[Y[i]] += 1
    union = sorted(list(set(x.keys()) & set(y.keys())), reverse = True)
    if not union:
        return "-1"
    elif union == ["0"]:
        return "0"
    for u in union:
        answer += u * min(x[u], y[u])
    return answer
    
    