from math import gcd

n = int(input())
arr = list(map(int, input().split()))
for idx in range(1, n):
    great = gcd(arr[0], arr[idx])
    print(f'{arr[0] // great}/{arr[idx] // great}')