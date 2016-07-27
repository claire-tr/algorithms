#coding=utf-8
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r, b = 0, len(nums) -1
        for i in xrange(0, b + 1):
            # First 2 then 0, order matters
            # Left/red part is already sorted, don't need to worry
            # 从左边换过来的不可能有2，但从右边换过来的可能有0
            # 在左指针左侧和右指针右侧的是sorted
            while nums[i] == 2 and i < b:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            while nums[i] == 0 and i > r:
                nums[i], nums[r] = nums[r], nums[i]
                r += 1
