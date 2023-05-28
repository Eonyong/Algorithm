import sys
import math
input = sys.stdin.readline


a, A = map(int, input().split())
b, B = map(int, input().split())

gcd = math.gcd(A * b + a * B, A * B)

print((A * b + a * B) // gcd, (A * B) // gcd)
