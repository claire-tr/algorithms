class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)


    def reverse(self, nums, i, j):
        while i>= 0 and j < len(nums) and i < j:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1