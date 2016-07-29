class Solution(object):
    # O(n)
    # Use hash map to store sum-index pair

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        sum, res= 0, 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum == k:
                res = max(res, i + 1)
            elif (sum - k) in dic:
                res = max(res, i - dic[sum - k])
            if sum not in dic:
                dic[sum] = i

        return res


    # O(n^2)
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = [0] * (len(nums) + 1)
        res = 0
        for i in xrange(1, len(nums) + 1):
            sum[i] = nums[i-1] + sum[i-1]

        for i in xrange(len(nums) + 1):
            for j in xrange(i + 1, len(nums) + 1):
                if sum[j] - sum[i] == k:
                    res = max(res, j - i)
        return res
