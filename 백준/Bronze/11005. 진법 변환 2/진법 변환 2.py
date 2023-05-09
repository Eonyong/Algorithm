import sys

input = sys.stdin.readline

answer = ''
db = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word, partial = map(int, input().split())
while word:
    word, mod = divmod(word, partial)
    answer = db[mod] + answer
print(answer)
