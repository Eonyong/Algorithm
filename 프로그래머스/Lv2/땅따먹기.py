def solution(land):
    answer = 0

    W = len(land)

    for start in range(4):
        pre_col = start
        ans = land[0][start]

        for row in range(1, W):
            high = [0, -1]

            for col in range(4):
                if pre_col != col and high[0] < land[row][col]:
                    high = [land[row][col], col]

            ans += high[0]
            pre_col = high[1]

        if answer < ans:
            answer = ans

    return answer


solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])
