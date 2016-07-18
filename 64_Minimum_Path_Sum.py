class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        dp = [0] * len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = dp[i-1] + grid[0][i]
        line = 1
        while line < len(grid):
            for i in range(0, len(grid[0])):
                if i == 0:
                    dp[i] += grid[line][0]
                else:
                    dp[i] = min(dp[i], dp[i-1]) + grid[line][i]
            line += 1
        return dp[len(grid[0])-1]
