import sys
from math import factorial

n = int(sys.stdin.readline())
two, one = n // 2, n - (n // 2) * 2
answer = 0
while two >= 0:
    answer += factorial(two + one) // (factorial(two) * factorial(one))
    two -= 1
    one += 2
print(answer % 10007)
