def solution(m, n, puddles):
    answer = 0
    boards = [[0 for _ in range(m)] for _ in range(n)]
    boards[0][0] = 1
        
    for row in range(n):
        for col in range(m):
            if not row and not col: continue
            if [col + 1, row + 1] in puddles:
                boards[row][col] = 0
            else:
                boards[row][col] = (boards[row - 1][col] + boards[row][col - 1]) % 1000000007
    
    print(boards)
    return boards[n - 1][m - 1]