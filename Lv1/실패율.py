def solution(N, stages):
    length = len(stages)
    level = {}
    for stage in range(1, N + 1):
        if length:
            cnt = stages.count(stage)
            level[stage] = cnt / length
            length -= cnt
        else:
            level[stage] = 0
    return sorted(level, key=lambda x: level[x], reverse=True)