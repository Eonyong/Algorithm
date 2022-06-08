from math import factorial

n, k = map(int, input().split())

m = factorial(n) // (factorial(k) * factorial(n -k))
print(m % 10007)