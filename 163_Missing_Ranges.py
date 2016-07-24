class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        i, n = 0, lower
        if not nums:
            return [self.getRange(lower, upper)]
        for i in xrange(len(nums)):
            if nums[i] != n:
                res.append(self.getRange(n, nums[i] -1))
                n = nums[i] + 1
            else:
                n += 1
        if nums[-1] != upper:
            res.append(self.getRange(n, upper))
        return res

    def getRange(self, n1, n2):
        # don't need to implement everytime
        if n1 == n2:
            return str(n1)
        else:
            return "%s->%s" % (n1, n2)