class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        # DFS will time limit exceeds

        # Number of islands is explore to the outside, this one is explore to shrink the size
        
        # Go through the border of the array, if meet O, replace the O at the border to 'Z', then explore from this O
        # Go thorugh the array, replace O with X
        # Go through the array, change 'Z' back to O
        if not board:
            return
        queue = []
        for i in range(len(board)):
            if board[i][0] == 'O':
                board[i][0] = 'Z'
                queue.append([i,0])
            if board[i][len(board[0])-1] == 'O':
                board[i][len(board[0])-1] = 'Z'
                queue.append([i, len(board[0])-1])
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                board[0][j] = 'Z'
                queue.append([0,j])
            if board[len(board)-1][j] == 'O':
                board[len(board)-1][j] = 'Z'
                queue.append([len(board)-1, j])


        while queue:
            i, j = queue.pop(0)
            if i + 1 < len(board) and board[i+1][j] == 'O':
                board[i+1][j] = 'Z'
                queue.append([i+1,j])
            if i - 1 >= 0 and board[i-1][j] == 'O':
                board[i-1][j] = 'Z'
                queue.append([i-1, j])
            if j + 1 < len(board[0]) and board[i][j+1] == 'O':
                board[i][j+1] = 'Z'
                queue.append([i,j+1])
            if j - 1 >= 0 and board[i][j-1] == 'O':
                board[i][j-1] = 'Z'
                queue.append([i, j-1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
