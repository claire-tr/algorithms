class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[start] = nums[i]
                start += 1
        for i in xrange(start, len(nums)):
            nums[i] = 0

        # One line Solution:
        #nums.sort(key= lambda x: 1 if x == 0 else 0)