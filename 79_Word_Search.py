class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        used = [[False] * len(board[0]) for _ in range(len(board))]
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    used[i][j] = True
                    if self.explore(board, word, used, i, j, 0):
                        return True
                    used[i][j] = False
        return False

    def explore(self, board, word, used, row, col, start):
        if start == len(word) - 1:
            return True
        for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[start + 1] and not used[i][j]:
                used[i][j] = True
                if self.explore(board, word, used, i, j, start + 1):
                    return True
                used[i][j] = False
        return False
