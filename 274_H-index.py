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

        # for i, c in enumerate(sorted(citations, reverse = True)):
        #     if i >= c:
        #         return i
        # return len(citations)

        # Extra space, but O(n) time
        n, h = len(citations), 0
        fre = [0] * (n + 1)
        for c in citations:
            if c >= n:
                fre[n] += 1
            else:
                fre[c] += 1

        for i in xrange(n, -1, -1):
            h += fre[i]
            if h >= i:
                return i
        return 0