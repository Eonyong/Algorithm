import sys


def power(n, r):
    if r == 1:
        return n % 1000000007
    elif r % 2:
        return (power(n, (r - 1) // 2) ** 2) * n % 1000000007
    elif not r % 2:
        return power(n, r // 2) ** 2 % 1000000007


K, P, N = map(int, sys.stdin.readline().split())

answer = (K * power(P, N)) % 1000000007

print(answer)
