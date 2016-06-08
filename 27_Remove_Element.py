class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        tail = 0
        for cur in range(len(nums)):
            if nums[cur] != val:
                nums[tail] = nums[cur]
                tail += 1
        return tail
