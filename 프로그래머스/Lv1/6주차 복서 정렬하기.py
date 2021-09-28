def solution(weights, head2head):
    plays = []  # 비교해 나갈 값을 저장하는 리스트

    for idx in range(len(weights)):
        player = weights[idx] # 경기를 진행할 선수를 지정합니다.

        fight = list(head2head[idx])    # player의 전적을 리스트로 불러옵니다.
        
        # higher(자신보다 무거운 선수 이긴 횟수), cnt(이긴 횟수), court(경기 횟수)
        higher, cnt, court = 0, 0, 0

        # player의 전적을 탐색
        for fi in range(len(fight)):
            # 경기를 치뤘으면
            if fight[fi] != 'N':
                # 경기횟수 1 추가
                court += 1
                # 만약 승리한 경기이면
                if fight[fi] == 'W':
                    # cnt 1 증가
                    cnt += 1
                    # 이긴 경기 중 자신보다 무거운 선수를 이겼을 경우 higher 1증가
                    if player < weights[fi]:
                        higher += 1

        # 전적을 다 돌고 난 후
        else:
            # 경기 횟수가 1이상이면
            if court:
                # 승률을 저장
                rate = cnt/court * 100
            else:
                # 승률을 0으로 지정
                rate = 0
        # 이제 [승률, 자신보다 무거운 선수 이긴 횟수, 선수 몸무게, 참가번호]를 저장
        plays.append([rate, higher, player, idx + 1])

    # 주어진 문제에 맞게 정렬을 진행, 아지막 참가번호만 오름차순...
    plays.sort(key=lambda x: [x[0], x[1], x[2], -x[3]], reverse=True)

    # 저장된 리스트의 등록번호 순으로 리스트 반환
    return list(map(list, zip(*plays)))[3]