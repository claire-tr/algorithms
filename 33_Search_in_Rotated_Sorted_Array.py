class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
            Two Cases:
                1. pivot is at the right half, aka nums[mid] > nums[r]
                    a. nums[l] < target < nums[mid]
                    b. else
                2. pivot is at the left half, aka nums[mid] < nums[r]
                    a. nums[mid] < target < nums[r]
                    b. else
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1