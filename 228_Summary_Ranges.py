class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                j = 1
                while i + j + 1 < len(nums) and nums[i+j+1] == nums[i+j] + 1:
                    j += 1
                res.append(str(nums[i]) + '->' + str(nums[i+j]))
                i = i + j + 1

            else:
                res.append(str(nums[i]))
                i += 1
        return res
