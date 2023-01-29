import sys

input = sys.stdin.readline


def MergeSort(arr, s, e):
    if s < e:
        middle = (s + e) // 2
        MergeSort(arr, s, middle)
        MergeSort(arr, middle + 1, e)
        Merge(arr, s, middle, e)


def Merge(arr, s, middle, e):
    global answer, m
    start, end = s, middle + 1
    tmp = []

    while start <= middle and end <= e:
        if arr[start] <= arr[end]:
            tmp.append(arr[start])
            start += 1
        else:
            tmp.append(arr[end])
            end += 1

    while start <= middle:
        tmp.append(arr[start])
        start += 1

    while end <= e:
        tmp.append(arr[end])
        end += 1

    start, idx = s, 0
    while start <= e:
        arr[start] = tmp[idx]
        m -= 1
        if m == 0:
            answer = tmp[idx]
        idx += 1
        start += 1


answer = -1
n, m = map(int, input().split())
boards = list(map(int, input().split()))

MergeSort(boards, 0, n - 1)
print(answer)