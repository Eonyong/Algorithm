# def solution(n, left, right):
#     answer = []
#     s_row, s_col = divmod(left, n)
#     e_row, e_col = divmod(right, n)
#     for row in range(s_row, e_row + 1):
#         if row == s_row:
#             lf = [row + 1] * row + list(range(row + 1, n + 1))
#             answer += lf[s_col:]
#         elif row == e_row:
#             rt = [row + 1] * row + list(range(row + 1, n + 1))
#             answer += rt[:e_col + 1]
#         else:
#             answer += [row + 1] * row + list(range(row + 1, n + 1))
#         print(answer)
#
#     return answer
# 로 푸는 건 줄 알았는데 하도 안풀려서 확인 해보니
def solution(n, left, right):
    return [max(divmod(i, n)) + 1 for i in range(left, right + 1)]


# 로 간단하게 불리는 문제였다....
# 너무 슬프다다

solution(3, 2, 5)
solution(4, 7, 14)
