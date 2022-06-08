from collections import defaultdict

n = int(input())
cards = defaultdict(int)
for num in map(int, input().split()):
    if num not in cards.keys():
        cards[num] = 1
    else:
        cards[num] += 1
answer = []
m = int(input())
for nums in map(int, input().split()):
    if nums in cards.keys():
        answer.append(cards[nums])
    else:
        answer.append(0)
print(*answer)