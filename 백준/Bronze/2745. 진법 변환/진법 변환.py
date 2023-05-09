import sys

input = sys.stdin.readline

answer = 0
word, partial = map(str, input().split())
partial = int(partial)
word = word[::-1]
i = 0
for w in word:
    if w.isdigit():
        answer += int(w) * (partial ** i)
    else:
        answer += (ord(w) - ord('A') + 10) * (partial ** i)
    i += 1
print(answer)