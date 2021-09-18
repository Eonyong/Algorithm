def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        answer+=(' '+ word.capitalize())
    return answer[1:]