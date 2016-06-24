class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Requirements: make sure that nums[1], nums[3], nums[5] ... is the Maxima

        for i in xrange(1, len(nums), 2):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            if i+1 < len(nums) and nums[i]< nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]