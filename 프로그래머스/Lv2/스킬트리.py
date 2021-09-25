def solution(skill, skill_trees):
    answer = 0
    N = len(skill)  # skill의 길이를 지정

    for skill_tree in skill_trees:
        # skill_tree안에 skill이 있으면 해당 인덱스를 skill_num에 추가, 없으면 99를 추가
        skill_num = [skill_tree.index(skill[idx]) if skill[idx] in skill_tree else 99 for idx in range(N)]
        
        # 스킬이 인덱스 순서대로 저장이 되어있는지 확인
        for lv in range(N - 1):
            # 만약 나중에 배워야하는 스킬을 먼저 배웠으면 break
            if skill_num[lv] > skill_num[lv + 1]:
                break
        # 순서대로 잘 배웠으면 answer 1을 증가
        else:
            answer += 1
            
    return answer