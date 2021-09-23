from pprint import pprint

def solution(m, n, board):
    answer = 0
    
    board = [list(ls) for ls in board]

    while True:
        position = []
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] == board[row][col+1] and board[row+1][col] == board[row+1][col+1] and board[row][col] == board[row+1][col] and board[row][col]:
                    position += [[row, col], [row, col+1], [row+1, col], [row+1, col+1]]

        for r, c in position:
            if board[r][c]:
                board[r][c] = 0
                answer += 1

        for row in range(1, m):
            for col in range(n):
                if not board[row][col]:
                    board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
        pprint(board)
        
        if not position:
            for row in range(m-1):
              for col in range(n-1):
                if board[row][col] == board[row][col+1] and board[row+1][col] == board[row+1][col+1] and board[row][col] == board[row+1][col] and board[row][col]:
                    position += [[row, col], [row, col+1], [row+1, col], [row+1, col+1]]

            for r, c in position:
                if board[r][c]:
                    board[r][c] = 0
                    answer += 1

            for row in range(1, m):
                for col in range(n):
                    if not board[row][col]:
                        board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
            return answer

print(solution(4, 4, ["ABCD", "BACE", "BCDD", "BCDD"]))