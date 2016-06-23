class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = set()
        for c in s:
            if c in dic:
                dic.remove(c)
            else:
                dic.add(c)
        return len(dic) <= 1
