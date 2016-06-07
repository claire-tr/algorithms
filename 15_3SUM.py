class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                # Note when it need to take care of the duplicates
                l, r = i+1, len(nums)-1
                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0:
                        res.append((nums[i], nums[l], nums[r]))
                        while l < r and nums[l+1] == nums[l]:
                            #inner loop needs to add constraints from outer loop
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        r -= 1

        return res