class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        '''
            Two pointers, flexible window size
            left pointer, the head, mark the start of the subarray
            right pointer, the i, scan through the array, mark the end of the subarray
            when sub_sum >= sum, update the minimum length, move left pointer forward
            With the two pointers scan at the "same" time, we can get linear runtime.
        '''
        res = float('inf')
        tsum, head = 0, 0
        for i in xrange(len(nums)):
            if tsum < s:
                tsum += nums[i]
            while tsum >= s:
                res = min(res, i - head + 1)
                tsum -= nums[head]
                head += 1
        return res if res <= len(nums) else 0