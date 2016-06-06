from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        d = defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in d:
                return[d[target-nums[i]], i]
            else:
                d[nums[i]] = i