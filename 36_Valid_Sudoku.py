class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.isPatiallyValid(board, 0, 9, i, i + 1):
                return False
            if not self.isPatiallyValid(board, i, i + 1, 0, 9):
                return False
            x, y = (i % 3) * 3, (i / 3) * 3
            if not self.isPatiallyValid(board, x, x + 3, y, y + 3):
                return False
        return True

    def isPatiallyValid(self, board, x1, x2, y1, y2):
        s = set()
        for i in xrange(x1, x2):
            for j in xrange(y1, y2):
                val = board[i][j]
                if val != '.':
                    if val not in s:
                        s.add(val)
                    else:
                        return False
        return True