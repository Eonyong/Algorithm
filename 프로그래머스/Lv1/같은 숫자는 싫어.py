def solution(arr):
    answer = []
    for idx in range(len(arr) - 1):
        if arr[idx] != arr[idx + 1]:
            answer.append(arr[idx])
    answer.append(arr[-1])
    return answer