class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pre = min_pre = maxhere = minhere = maxsofar = nums[0]
        # Because it need to be contiguous, so every max/minhere need to **end at current element***(have to have the current element)
        for i in range(1, len(nums)):
            maxhere = max(nums[i], max_pre * nums[i], min_pre * nums[i])
            minhere = min(nums[i], max_pre * nums[i], min_pre * nums[i])
            max_pre, min_pre = maxhere, minhere
            maxsofar = max(maxsofar, maxhere)
        return maxsofar
