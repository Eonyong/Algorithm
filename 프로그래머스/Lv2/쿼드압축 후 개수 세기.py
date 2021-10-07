# 각 사분면의 사각형을 받아오는 함수 식
def quad_mini(array, si, ei, sj, ej):
    square = []
    for i in range(si, ei):
        row = []
        for j in range(sj, ej):
            row.append(array[i][j])
        square.append(row)
    return square

def quad(array, cnt):
    N = len(array)  # 정사각형의 N * N의 값을 가져옵니다.

    # 좌 상단을 가준으로 시겨방향으로 나눠진 사각형을 저장하는 box리스트를 생성
    box = [quad_mini(array, 0, N//2, 0, N//2), quad_mini(array, 0, N//2, N//2, N),
          quad_mini(array, N//2, N, 0, N//2), quad_mini(array, N//2, N, N//2, N)]
    
    # box를 순회하면서 박스 안의 전체값이 0이나 1이면 cnt의 값을 증가 시켜줌
    for l in box:
        if sum(map(sum, l)) == len(l) ** 2:
            cnt[1] += 1
        elif not sum(map(sum, l)):
            cnt[0] += 1
        # 전부 0이나 1이 아니면 다시 quad 함수를 반복
        else:
            quad(l, cnt)

def solution(arr):
    
    cnt = [0, 0]
    
    # 시작할 때 주어진 arr 값 자체가 전부 0이거나 1인 경우 반환하는 리스트 
    if sum(map(sum, arr)) == len(arr) ** 2:
        return [0, 1]
    elif not sum(map(sum, arr)):
        return [1, 0]
    else:
        quad(arr, cnt)
        return cnt