from math import gcd
def solution(n, m):
    min_val = gcd(n, m)
    answer = [min_val, gcd(n, m) * (n / min_val) * (m / min_val)]
    return answer