class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l, r = 0, x
        while l < r:
            mid = l + (r - l)/2
            if mid * mid > x:
                r = mid - 1
            else:
                if mid * mid <= x < (mid + 1) * (mid + 1):
                    return mid
                else:
                    l = mid + 1
        return l
