class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxEndingHere = -sys.maxint
        maxSoFar = -sys.maxint

        for n in nums:
            maxEndingHere = max(maxEndingHere + n, n)
            maxSoFar = max(maxEndingHere, maxSoFar)
        return maxSoFar
