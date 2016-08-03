class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # index indicates how many paper have more citations than the current one
        # n - i : # papers, which have greater or equal citations with the current one
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l)/2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        # result may be l
        # (We are looking for the first position that f is greater than or equal to the position)
        return n - l
