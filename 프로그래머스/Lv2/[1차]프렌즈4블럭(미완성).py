from pprint import pprint

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]

    while True:
        blocks = set()
        for row in range(m - 1):
            for col in range(n - 1):
                if board[row][col] and board[row][col] == board[row + 1][col] == board[row][col + 1] == board[row + 1][col + 1]:

                    blocks.add((row, col))
                    blocks.add((row + 1, col))
                    blocks.add((row, col + 1))
                    blocks.add((row + 1, col + 1))

        for row, col in blocks:
            board[row][col] = 0

        answer += len(blocks)

        for row in range(1, m):
            for col in range(n):
                if not board[row][col]:
                    board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
        pprint(board)
        print()

        if not blocks:
            break

    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
