import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
packets = deque()

while True:
    m = int(input())
    if m == -1:
        break
    elif not m:
        packets.popleft()
    else:
        if len(packets) < n:
            packets.append(m)
if packets:
    print(*packets)
else:
    print("empty")