class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Could also solve by detecting cycle -> O(1) Space
        # https://discuss.leetcode.com/topic/12587/my-solution-in-c-o-1-space-and-no-magic-math-property-involved
        dic = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in dic:
                return False
            else:
                dic.add(n)
        return True