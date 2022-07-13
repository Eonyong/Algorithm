import sys

words = sys.stdin.readline().strip()
arr, alphabet = [], [0] * 26

for word in words:
    alphabet[ord(word) - ord('a')] += 1
    arr += [alphabet[:]]

for _ in range(int(sys.stdin.readline())):
    v, s, e = sys.stdin.readline().split()
    print(arr[int(e)][ord(v) - ord('a')] - arr[int(s) - 1][ord(v) - ord('a')]) if int(s) else print(arr[int(e)][ord(v) - ord('a')])
