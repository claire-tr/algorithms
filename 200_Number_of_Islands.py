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

# Using Stack to do iteratively

