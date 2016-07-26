class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Consider that each local maximum is one valid peak.
        Find one local maximum with binary search.
        l, r pointer trying to reaches the local higher element(around mid)
        Finally will find the local maximum
        Binary search satisfies the O(logn) computational complexity.
        '''
        l, r = 0, len(nums)-1
        while l < r:
            mid1 = l + (r - l)/2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                l = mid2
            else:
                r = mid1
        return l