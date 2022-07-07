commands = [list(input()) for _ in range(int(input()))]
answer = ''
for command in zip(*commands):
    answer = answer + command[0] if len(set(command)) == 1 else answer + '?'
print(answer)