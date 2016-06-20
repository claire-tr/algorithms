class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        res[0] = 1
        # Pay attention to the connections/patterns between

        # Two rounds

        # 1. Multiply all the numbers at the left
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        # 2. Multiply all the numbers at the right
        #   Cannot use the array itself to record anymore
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res