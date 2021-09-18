def solution(arr1, arr2):
    answer = []
    arr2 = list(map(list, zip(*arr2)))
    for x in arr1:
        row = []
        for y in arr2:
            row.append(sum([a*b for a, b in zip(x, y)]))
        answer.append(row)
    return answer