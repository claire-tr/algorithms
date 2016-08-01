#coding=utf-8
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b


def knows(a, b):
    pass


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
            The idea is as follows:
            First, the elimination process. If the left people knows right, we will eliminate left person,
            which is left += 1; else, we will eliminate the right person, which is the step right -= 1.
            After we go through all these steps, we will know that only one person is left that satisfies our logic.
            Second, we check two things after we get this candidate.
            1. If this candidate knows other person in the group, if the candidate knows anyone in the group,
            then the candidate is not celebrity, return -1;
            2. if everyone knows this candidate, if anyone does not know the candidate, return -1;
        '''
        l, r = 0, n-1
        while l < r:
            if knows(l, r):
                l += 1
            else:
                r -= 1
        for i in xrange(n):
            if i != l:
                if knows(l, i) or not knows(i, l):
                    return -1
        return l