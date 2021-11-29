answer = 0
# 입력을 받는 부분
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 각 강의실 마다 학생 수를 확인하며
for student in A:
    # 먼저 감독관이 감독할 수 있는 학생의 수를 구하고 감독한 학생의 수를 빼준다
    answer += 1
    student -= B
    # 이후에 감독이 필요한 학생이 남는 경우, 부감독관의 수를 구하기 위한 코드
    if student > 0:
        # 나머지가 0이 아닌 경우, 학생수를 부감독관이 감시할 수 있는 학생 수로 나눈 뒤 1을 더해준다.
        if student % C:
            answer += student // C + 1

        # 0인 경우에는 학생수를 부감독관이 감시할 수 있는 학생 수로 나눈 값만 더해준다.
        else:
            answer += student // C
# 정답 출력
print(answer)