class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Similar to Binary transfer, it's a 26-nary representation
        res = 0
        for i in range(len(s)):
            print i
            res += (ord(s[len(s) - 1 - i]) - ord('A') + 1) * pow(26, i)
        return res