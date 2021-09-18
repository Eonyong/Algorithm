def solution(s):
    answer = []
    cnt = 0
    length = 0
    while s != '1':
        a = len(s)
        s = s.replace('0', '')
        length += (a - len(s))
        cnt += 1
        s = bin(len(s))[2:]
    return [cnt, length]