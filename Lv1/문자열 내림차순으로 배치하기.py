def solution(s):
    answer = ''
    s_ord = []
    for i in s:
        s_ord.append(ord(i))
    s_ord.sort(reverse=True)
    for num in s_ord:
        answer += chr(num)
    return answer