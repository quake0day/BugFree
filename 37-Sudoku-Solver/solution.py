class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(i, j):
            tmp = board[i][j] 
            board[i][j] = 'D'
            for x in xrange(9):
                if board[i][x] == tmp:
                    return False
            for y in xrange(9):
                if board[y][j] == tmp:
                    return False
            for z in range(3):
                for q in range(3):
                    if board[(i/3)*3+z][(j/3)*3+q] == tmp:
                        return False
            board[i][j] = tmp
            return True
        def dfs(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
        dfs(board)
    
