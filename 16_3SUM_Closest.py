class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l, r = i+1, len(nums)-1
                while l < r:
                    temp = nums[i] + nums[l] + nums[r]
                    if abs(temp-target) == 0:
                        return temp
                    elif temp < target:
                        l += 1
                    else:
                        r -= 1
                    if abs(temp-target) < abs(res-target):
                        res = temp
        return res