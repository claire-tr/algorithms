class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) != 9 or len(board[0]) != 9:
            return
        self.helper(board, 0, 0)

    def helper(self, board, i, j):
        if j >= 9:
            return self.helper(board, i + 1, 0)
        if i == 9:
            return True
        # print i, j
        if board[i][j] == '.':
            for k in xrange(1, 10):
                board[i][j] = str(k)
                if self.isValid(board, i, j):
                    if self.helper(board, i, j + 1):
                        return True
                board[i][j] = '.'
        else:
            return self.helper(board, i, j + 1)
        return False

    def isValid(self, board, i, j):
        for k in xrange(9):
            if k != j and board[i][k] == board[i][j]:
                return False
        for k in xrange(9):
            if k != i and board[k][j] == board[i][j]:
                return False
        for row in xrange(i/3*3, i/3*3 + 3):
            for col in xrange(j/3*3, j/3*3 + 3):
                if (row != i or col != j) and board[row][col] == board[i][j]:
                    return False
        return True