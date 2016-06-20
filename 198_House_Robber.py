class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        return dp[len(nums)]
