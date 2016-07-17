# coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        return self.bsearch(nums, 0, len(nums)-1)

    def bsearch(self, nums, l, r):

        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            mid = l + (r-l)/2
            if nums[mid] >= nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]

    def bsearch_II(self, nums, l, r):
        # 分两种情况讨论
        while l < r:
            mid = l + (r-l)/2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[r]