# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        mid = l + (r - l)/2
        while guess(mid) != 0:
            if guess(mid) == 1:
                l = mid + 1
            else:
                r = mid - 1
            mid = l + (r - l)/2
        return mid