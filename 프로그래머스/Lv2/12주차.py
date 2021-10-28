def solution(k, dungeons):
    
    # 일단 순열을 만드는 함수를 만들어 줍니다
    def soon(i, N, choose, arr):
        ls = []
        if i == N:
            return [arr]
        else:
            for j in range(N):
                if not choose[j]:
                    choose[j] = 1
                    ls += soon(i + 1, N, choose, arr + [j])
                    choose[j] = 0
        return ls
            
    # 던전을 들리는 모든 경우의 수를 저장
    sources = soon(0, len(dungeons), [0] * len(dungeons), [])
    answer = -1
    
    # 모든 경우의 수를 탐색
    for source in sources:
        life = k    # 피로도를 copy해서 저장
        ans = 0 # 각 경우의 수에서 던전을 들리는 경우의 수를 저장
        # 각 경우의 수에서의 던전을 클리어
        for s in source:
            if dungeons[s][0] <= life:
                life -= dungeons[s][1]
                ans += 1
            else:
                break
        # 다 돌고 낙서 이전의 최고 던전 경우의 수보다 크면
        # answer 수정
        if answer < ans:
            answer = ans
    
    return answer