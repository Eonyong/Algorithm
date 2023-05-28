import sys

input = sys.stdin.readline


member = set()
answer = 0
for _ in range(int(input())):
    sign = input().rstrip()
    if 'ENTER' == sign:
        answer += len(member)
        member = set()
    else:
        if sign not in member:
            member.add(sign)
answer += len(member)
print(answer)