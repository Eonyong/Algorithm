def solution(lottos, win_nums):
    min_win = len(set(lottos) & set(win_nums))
    max_win = min_win + lottos.count(0)
    answer = [max_win, min_win]
    
    for rank in range(len(answer)):
        if answer[rank] == 6:
            answer[rank] = 1
        elif answer[rank] == 5:
            answer[rank] = 2
        elif answer[rank] == 4:
            answer[rank] = 3
        elif answer[rank] == 3:
            answer[rank] = 4
        elif answer[rank] == 2:
            answer[rank] = 5
        else:
            answer[rank] = 6
    
    return answer