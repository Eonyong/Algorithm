def solution(arr1, arr2):
    answer = []
    while arr1:
        ar = []
        a = arr1.pop(0)
        b = arr2.pop(0)
        for idx in range(len(a)):
            ar.append(a[idx] + b[idx])
        answer.append(ar)
    return answer