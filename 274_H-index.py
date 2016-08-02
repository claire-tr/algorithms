class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        '''
        First we order the values of f from the largest to the lowest value. Then, we look for the last position in
        which f is greater than or equal to the position (we call h this position).
        '''

        for i, c in enumerate(sorted(citations, reverse = True)):
            if i >= c:
                return i
        return len(citations)