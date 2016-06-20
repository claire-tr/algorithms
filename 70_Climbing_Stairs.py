class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        # O(1) Space
        # Two: two steps before == dp[i-2]
        # One: one step before == dp[i-1]
        two, one = 1, 2
        for i in range(3, n+1):
            all = one + two
            two = one
            one = all

        return all