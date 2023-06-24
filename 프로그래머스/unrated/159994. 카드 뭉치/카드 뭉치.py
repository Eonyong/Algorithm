def solution(cards1, cards2, goal):
    one, two, thr = 0, 0, 0
    for idx in range(len(goal)):
        if one < len(cards1) and cards1[one] == goal[idx]:
            one += 1
        elif two < len(cards2) and cards2[two] == goal[idx]:
            two += 1
        else:
            return "No"
    return "Yes"