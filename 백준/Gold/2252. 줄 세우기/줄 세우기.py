import sys
from collections import deque
input = sys.stdin.readline

# https://sungmin-joo.tistory.com/83 참조
n, m = map(int, input().split())

answer = []
ls = deque()
degrees = [[] for _ in range(n + 1)]
cnts = [0 for _ in range(n + 1)]

refs = [list(map(int, input().split())) for _ in range(m)]

# 입력 받은 값들 중 편도(a가 b 보다 앞에 와야하는) 조건 이므로
# cnts의 b-index의 값을 1 상승 시켜주고 degrees의 a-index 배열에 b를 추가해준다.
for a, b in refs:
    cnts[b] += 1
    degrees[a].append(b)

# 전체 index를 탐색하면서 참조를 하지 않아도 되는 값(cnts[index]가 0)들을 ls에 추가 해준다.
for idx in range(1, n + 1):
    if not cnts[idx]:
        ls.append(idx)

# 이제 ls에 저장된 값들을 순서대로 빼내고
# 해당 값이 참조하고 있는 index의 cnts 1 감소
# 참조된 index의 cnts가 0이 되면 ls에 추가
# 해당 루틴을 ls가 []가 될 때까지 진행 (모든 값을 정렬하기 위해서이다.)
while ls:
    start = ls.popleft()
    answer.append(start)
    for e in degrees[start]:
        cnts[e] -= 1
        if not cnts[e]:
            ls.append(e)

# 출력
print(*answer)