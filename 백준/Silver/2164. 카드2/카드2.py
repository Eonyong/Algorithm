from collections import deque

cards = deque(range(1, int(input()) + 1))
if len(cards) > 1:
    while True:
        cards.popleft()
        if len(cards) > 1:
            cards.rotate(-1)
        else:
            break
print(cards.pop())