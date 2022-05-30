words = list(input())
n = len(words)
answer = []
for s in range(1, n - 1):
    for e in range(s + 1, n):
        first, second, third = reversed(words[:s]), reversed(words[s:e]), reversed(words[e:])
        answer.append(list(first) + list(second) + list(third))
answer.sort()
print(''.join(answer[0]))