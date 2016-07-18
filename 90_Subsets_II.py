class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.helper(sorted(nums), [], results)
        return results

    def helper(self, nums, res, results):
        results.append([r for r in res])
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            res.append(n)
            self.helper(nums[i+1:], res, results)
            res.pop()