class Solution(object):
    def combinationSum4_recur(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # So we know that target is the sum of numbers in the array.
        # Imagine we only need one more number to reach target, this number can be any one in the array, right?
        # So the # of combinations of target, comb[target] = sum(comb[target - nums[i]]),
        # where 0 <= i < nums.length, and target >= nums[i].
        if target == 0:
            return 1
        if target < 0:
            return 0
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.combinationSum4_recur(nums, target - nums[i])
        return res

    def combinationSum4_topDown(self, nums, target):
        # Now for a DP solution, we just need to figure out a way to store the intermediate results,
        # to avoid the same combination sum being calculated many times. We can use an array to save those results,
        # and check if there is already a result before calculation.
        # We can fill the array with -1 to indicate that the result hasn't been calculated yet.
        # 0 is not a good choice because it means there is no combination sum for the target.
        dp = [-1] * (target + 1)
        dp[0] = 1

        def helper(nums, target):
            if dp[target] != -1:
                return dp[target]
            res = 0
            for i in range(0, len(nums)):
                if target >= nums[i]:
                    res += self.helper(nums, target - nums[i])
            dp[target] = res
            return res

        return helper(nums, target)

    def combinationSum4(self, nums, target):
        # Bottom up
        comb = [0] * (target + 1)
        comb[0] = 1
        for i in range(1, len(comb)):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    comb[i] += comb[i-nums[j]]
        return comb[target]

