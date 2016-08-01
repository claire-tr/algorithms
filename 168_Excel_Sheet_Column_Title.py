class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            n -= 1
            res = chr(ord('A') + n % 26) + res
            n /= 26
        return res
