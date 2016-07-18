class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in sorted(nums):
            for i in xrange(len(res)):
                res.append(res[i] + [n])
        return res