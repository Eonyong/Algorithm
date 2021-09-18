def solution(table, languages, preference):
    answer = ''
    top = 0
    score = [[l, p] for l, p in zip(languages, preference)]
    for t in table:
        total = 0
        t = t.split(' ')
        for l, p in score:
            if l in t:
                total += (6 - t.index(l))*p
        if total > top:
            top = total
            answer = t[0]
        elif total == top:
            if ord(answer[0]) > ord(t[0][0]):
                answer = t[0]
                
        
    return answer