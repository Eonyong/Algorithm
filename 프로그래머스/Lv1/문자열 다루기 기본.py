def solution(s):
    # isdigit 자체가 숫자인지 판단하는 함수이다.
    return True if s.isdigit() and (len(s) == 4 or len(s) == 6) else False