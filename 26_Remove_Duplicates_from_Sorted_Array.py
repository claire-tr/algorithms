class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Notice the differences between No.80, for this approach, it improves so that we
        # don't have to handle the corner cases with extra code as in No. 80
        i = 0
        for n in nums:
            if i < 1 or n != nums[i-1]:
                nums[i] = n
                i += 1
        return i