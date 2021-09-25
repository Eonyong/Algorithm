from math import gcd # 최대공약수를 이용하여 최소공배수(lcm) 구하기
def solution(arr):

    answer = arr.pop() # arr의 값 하나를 answer에 저장

    # arr 리스트 값이 존재하면 진행
    while arr:
        # arr 값 하나 저장
        val = arr.pop()
        # 최대공약수 값 저장
        gcd_val = gcd(answer, val)
        # 최대공약수와 각 수를 최대공약수로 나눈 몫들을 곱해서 lcm 저장
        answer =  gcd_val * (answer // gcd_val) * (val // gcd_val)
    return answer


solution([2,6,8,14])