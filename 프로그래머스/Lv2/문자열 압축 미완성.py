from itertools import groupby

def solution(s):
    answer = 0
    for i in groupby(s, key=s):
        print(i[0], list(i[1]))
    print('___________')
    return answer


solution("aabbaccc")    # 7
solution("ababcdcdababcdcd")    # 9
solution("abcabcdede")  # 8
solution("abcabcabcabcdededededede")    # 14
solution("xababcdcdababcdcd")   # 17