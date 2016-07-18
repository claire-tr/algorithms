class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = sys.maxint
        dp = [0] + [MAX] * amount

        for i in range(1, len(dp)):
                dp[i] = min(dp[i-c] if i - c >= 0 else MAX for c in coins) + 1

        return dp[amount] if dp[amount] < sys.maxint else -1