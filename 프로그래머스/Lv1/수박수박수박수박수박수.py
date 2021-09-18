def solution(n):
    if n % 2:
        return '수박'*((n-1)//2) + '수'
    else:
        return '수박'*(n//2)