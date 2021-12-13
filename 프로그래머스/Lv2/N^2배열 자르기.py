def solution(n, left, right):
    answer = []
    s_row, s_col = divmod(left, n)
    e_row, e_col = divmod(right, n)
    for row in range(s_row, e_row + 1):
        if row == s_row:
            lf = [row + 1] * row + list(range(row + 1, n + 1))
            answer += lf[s_col:]
        elif row == e_row:
            rt = [row + 1] * row + list(range(row + 1, n + 1))
            answer += rt[:e_col + 1]
        else:
            answer += [row + 1] * row + list(range(row + 1, n + 1))

    return answer


solution(3, 2, 5)
solution(4, 7, 14)
