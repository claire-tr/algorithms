class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res, base = 10, 9
        for i in xrange(2, min(n, 10) + 1):
            base *= (9 - i + 2)
            res += base

        return res
