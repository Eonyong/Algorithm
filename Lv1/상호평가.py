def avg_score(avg):
    if avg >= 90:
        return 'A'
    elif avg >=80:
        return 'B'
    elif avg >=70:
        return 'C'
    elif avg >=50:
        return 'D'
    else:
        return 'F'
    
def solution(scores):
    answer = ''
    N = len(scores)
    scores = list(map(list, zip(*scores)))
    for i in range(N):
        if scores[i][i] == min(scores[i]) and scores[i].count(min(scores[i])) == 1:
            avg = (sum(scores[i]) - scores[i][i]) / (N - 1)
        elif scores[i][i] == max(scores[i]) and scores[i].count(max(scores[i])) == 1:
            avg = (sum(scores[i]) - scores[i][i]) / (N - 1)
        else:
            avg = sum(scores[i]) / N
        answer += avg_score(avg)
    
    return answer