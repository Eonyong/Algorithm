def solution(s):
    answer = []
    s = s.replace('{{', '')
    s = s.replace('}}', '')
    s = s.split('},{')
    s.sort(key=lambda x: len(x))
    for i in s:
        i = i.split(',')
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer