from itertools import permutations
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# case = [[0] * 3 for _ in range(3)]
# for row in range(3):
#     for col in range(3):
#         case[col][3 - row - 1] = arr[row][col]
# print(case)

N, M, tc = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tests = [list(map(int, input().split())) for _ in range(tc)]
testCase = list(permutations(range(len(tests))))

for test in testCase:
    paste = arr
    for t in test:
        rotate = [arr[row][tests[t][1] - tests[t][2] - 1: tests[t][1] + tests[t][2]] for row in range(tests[t][0] - tests[t][2] - 1, tests[t][0] + tests[t][2])]
