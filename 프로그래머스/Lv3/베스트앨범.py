from collections import defaultdict


# 해당 문제는 장르별 총 길이를 구하고 이를 활용해 장르별 재생 횟수가 많은 두개를 추출하는 방식
# defaultdict에 익숙해지기 위해 이를 이용하여 문제를 풀었습니다.
def solution(genres, plays):
    answer = []
    # 각 장르의 총 길이를 구하기 위해 만든 딕셔너리
    genre_length = defaultdict(int)
    # 장르별 각 재생 횟수와 인덱스값을 저장하기 위한 딕셔너리
    genre_per_idx = defaultdict(list)
    # 인덱스를 순회하면서 장르의 총 길이와 노래별 길이와 인덱스를 딕셔너리에 저장합니다.
    for idx in range(len(genres)):
        genre_length[genres[idx]] += plays[idx]
        genre_per_idx[genres[idx]].append([plays[idx], idx])
    # 총 재생횟수가 큰 것을 우선순위로 두므로 총 길이에 따라 이를 오름차순으로 정렬 합니다.
    genre_length = sorted(genre_length.items(), key=lambda x: x[1])

    # 모든 장르를 탐색하며 각 장르별 최대 두개씩 뽑아 내는 while문을 작성
    while genre_length:
        # 길이를 버리고 장르만 뽑아내서 장르 길이를 오름차순, 인덱스를 내림차순으로 정렬
        genre, _ = genre_length.pop()
        length_per_idx = sorted(genre_per_idx[genre], key=lambda x: (x[0], -x[1]))
        # 해당 장르의 노래 중 길이 순, 인덱스가 작은 순으로 두개를 뽑아서 answer 추가
        # 만약 해당 장르에 노래가 한 곡 뿐이면 하나만 뽑아서 인덱스를 저장
        if len(length_per_idx) > 1:
            for _ in range(2):
                _, index = length_per_idx.pop()
                answer.append(index)
        else:
            _, index = length_per_idx.pop()
            answer.append(index)

    return answer
