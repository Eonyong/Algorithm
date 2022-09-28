import sys
input = sys.stdin.readline


def Recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return Recursion(s, l + 1, r - 1, cnt + 1)


def Pelindrome(words):
    return Recursion(words, 0, len(words) - 1, 1)


for _ in range(int(input())):
    print(*Pelindrome(input().strip()))
