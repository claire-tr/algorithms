class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Since it is UNSORTED, why not just turn them into a set
            https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak
            First turn the input into a set of numbers.
            That takes O(n) and then we can ask in O(1) whether we have a certain number.

            Then go through the numbers. If the number n is the start of a streak (i.e., n-1 is not in the set),
            then test m = n+1, n+2, n+3, ... and stop at the first number m not in the set.
            The length of the streak is then simply m-n and we update our global best with that.
            Since we check each streak only once, this is overall O(n).
        '''
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(m - n, best)

        return best