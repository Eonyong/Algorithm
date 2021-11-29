def solution(n, words):
    # 저장소 를 만들어 줍니다.
    store = set()

    for i in range(len(words) - 1):
        # 인덱스 값을 두개 비교하며 진행
        if words[i][-1] != words[i + 1][0]:
            # 만약 앞의 끝 단어와 뒤의 첫 단어가 다르면 뒤의 인덱스를 n으로 나눈 나머지 + 1과 rotate 수를 반환
            return [(i + 1) % n + 1, (i + 2) // n + 1 if (i + 2) % n else (i + 2) // n]
        else:
            if words[i] in store:
                # 만약 단어가 저장소에 들어 있으면 앞의 인덱스를 n으로 나눈 나머지 + 1과 rotate 수를 반환
                return [i % n + 1, (i + 1) // n + 1 if (i + 1) % n else (i + 1) // n]
            else:
                # 그게 아니면 앞의 단어를 저장소에 저장
                store.add(words[i])
                if words[i + 1] in store:
                    # 만약 단어가 저장소에 들어 있으면 뒤의 인덱스를 n으로 나눈 나머지 + 1과 rotate 수를 반환
                    return [(i + 1) % n + 1, (i + 2) // n + 1 if (i + 2) % n else (i + 2) // n]
    #  전부 돌았는데 틀린게 없으면 [0, 0]을 반환
    else:
        return [0, 0]