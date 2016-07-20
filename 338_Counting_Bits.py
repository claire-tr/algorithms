class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # dp[i] = dp[i / 2] + i % 2.
        dp = [0] * (num + 1)
        for i in xrange(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
