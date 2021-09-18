def solution(brown, yellow):
    return [(brown // 2 + ((brown // 2 - 2)**2 - 4 * yellow)**.5) / 2 + 1, (brown // 2 - ((brown // 2 - 2)**2 - 4 * yellow)**.5) / 2 + 1]