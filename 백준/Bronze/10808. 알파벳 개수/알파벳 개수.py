import sys

input = sys.stdin.readline

alphabet = [0 for _ in range(97, 123)]

names = input().rstrip()

for name in names:
    alphabet[ord(name) - ord('a')] += 1
   
print(*alphabet)