import sys
from math import gcd

n = int(sys.stdin.readline())
ls = []
result = []

for _ in range(n):
    ls.append(int(sys.stdin.readline()))
ls.sort()

temp = [ls[i] - ls[i - 1] for i in range(1, n)]
my_gcd = temp[0]

for i in range(1, n - 1):
    my_gcd = gcd(my_gcd, temp[i])

for i in range(1, int(pow(my_gcd, 1 / 2)) + 1):

    if my_gcd % i == 0:
        if i ** 2 == my_gcd:
            result.append(i)
        else:
            result += [i, my_gcd // i]

result.sort()

print(*result[1:])