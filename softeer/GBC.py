N, M = map(int, input().split())

elevator = [0] * 100

sector_per_limit = [list(map(int, input().split())) for _ in range(N)]
gwang_woo_test = [list(map(int, input().split())) for _ in range(M)]

start = 0
for sector, vector in sector_per_limit:
    for sec in range(start, sector + start):
        elevator[sec] = vector
    else:
        start += sector

answer = 0
start = 0
for sector, vector in gwang_woo_test:
    for sec in range(start, sector + start):
        if vector > elevator[sec]:
            over_vector = abs(elevator[sec] - vector)
            if answer < over_vector:
                answer = over_vector
    else:
        start += sector

print(answer)