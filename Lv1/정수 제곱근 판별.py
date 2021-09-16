def solution(n):
    # 제곱근의 정수형이 제곱근의 값과 같으면 제곱근 + 1의 제곱을 리턴하고, 아니면 -1
    return (int(n**.5)+1)**2 if int(n**.5) == n**.5 else -1