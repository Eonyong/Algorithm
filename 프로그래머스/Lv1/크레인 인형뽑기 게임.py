def solution(board, moves):
    answer = 0
    box = []
    board = list(map(list, zip(*board)))
    while moves:
        move = moves.pop(0)
        line = board[move - 1]

        if any(line):
            for idx in range(len(line)):
                if line[idx]:
                    icon, line[idx] = line[idx], 0
                    box.append(icon)
                    break

        if len(box) > 1:
            a = box.pop()
            b = box.pop()
            if a == b:
                answer += 2
            else:
                box += [b, a]
    return answer