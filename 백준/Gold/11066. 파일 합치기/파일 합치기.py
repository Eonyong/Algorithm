import sys
# from pprint import pprint
input = sys.stdin.readline


for _ in range(int(input())):
    answer = float('inf')
    n = int(input())
    ls = list(map(int, input().split()))
    s = [0]
    boards = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for idx in range(1, n + 1):
        boards[idx - 1][idx] = idx
        s.append(s[-1] + ls[idx - 1])

    for row in range(2, n + 1):
        for col in range(n - row + 1):
            j = row + col
            dp[col][j] = sys.maxsize

            for k in range(boards[col][j - 1], boards[col + 1][j] + 1):
                minNum = dp[col][k] + dp[k][j] + s[j] - s[col]
                if dp[col][j] > minNum:
                    dp[col][j] = minNum
                    boards[col][j] = k
            # print(f"{boards[col][j - 1]} ~ {boards[col + 1][j] + 1} => row: {row}, col: {col}, j: {j}")
            # print("boards ----")
            # pprint(boards)
            # print("dp -----")
            # pprint(dp)
            # print()

    print(dp[0][-1])