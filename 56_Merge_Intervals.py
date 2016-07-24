# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
            "Keep updating the endpoint"
            Sort the intervals by their starting points.
            for each interval in the sorted intervals, compare the start point of current
            interval and the end point of the last interval that is already in the result list
            If they overlap, set the end point of the interval as the longest end point among this two.
        '''
        res = []
        sort = sorted(intervals, key=lambda i: i.start)
        for s in sort:
            if res and s.start <= res[-1].end:
                res[-1].end = max(res[-1].end, s.end)
            else:
                res.append(s)
        return res