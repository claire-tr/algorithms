class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        '''
            One more case, like [1, 1, 3, 1]
                r -= 1
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)/2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r -= 1
        return False