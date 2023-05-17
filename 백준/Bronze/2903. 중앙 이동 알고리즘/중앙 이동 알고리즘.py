import sys

input = sys.stdin.readline

n = int(input())
step = 2

for _ in range(n):
    step += (step - 1)
    
print(pow(step, 2))
