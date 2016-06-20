# Recursively (DFS)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.explore(grid, i, j)
                    # print i, j
                    cnt += 1
        return cnt

    def explore(self, grid, i, j):
        grid[i][j] = 'x'
        tmp = i
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.explore(grid, i - 1, j)
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.explore(grid, i, j - 1)
        if i + 1 < len(grid) and grid[i+1][j] == '1':
            self.explore(grid, i + 1, j)
        if j + 1 < len(grid[0]) and grid[i][j+1] == '1':
            self.explore(grid, i, j + 1)

# Using Queue to do iteratively
# Need to pay extra attention, because the order will change

class Solution(object):
    def numIslands(self, grid):

        if not grid:
            return 0
        cnt = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = 'x'
                    while queue:
                        a, b = queue.pop(0)
                        if a+1 < len(grid) and grid[a+1][b] == '1':
                            grid[a+1][b] = 'x'
                            queue.append((a+1, b))
                        if a-1 >= 0 and grid[a-1][b] == '1':
                            grid[a-1][b] = 'x'
                            queue.append((a-1, b))
                        if b+1 < len(grid[0]) and grid[a][b+1] == '1':
                            grid[a][b+1] = 'x'
                            queue.append((a, b+1))
                        if b-1 >= 0 and grid[a][b-1] == '1':
                            grid[a][b-1] = 'x'
                            queue.append((a, b-1))
                    cnt += 1

        return cnt
        

