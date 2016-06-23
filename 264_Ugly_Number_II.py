class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i1, i2, i3 = 0, 0, 0
        while n > 1:
            u1, u2, u3 = 2 * ugly[i1], 3 * ugly[i2], 5 * ugly[i3]
            umin = min(u1, u2, u3)
            ugly.append(umin)
            if umin == u1:
                i1 += 1
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            n -= 1
        return ugly[-1]