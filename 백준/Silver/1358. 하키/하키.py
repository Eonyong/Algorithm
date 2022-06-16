w, h, x, y, p = map(int ,input().split())
radius = h // 2
answer = 0
for _ in range(p):
    c, r = map(int, input().split())
    if x <= c <= x + w and y <= r <= y + h or ((c - x) ** 2 + (r - y - radius) ** 2) ** .5 <= radius or ((c - x - w) ** 2 + (r - y - radius) ** 2) ** .5 <= radius:
        answer += 1
print(answer)