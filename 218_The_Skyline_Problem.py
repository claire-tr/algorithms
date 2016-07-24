from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
            # https://briangordon.github.io/2014/08/the-skyline-problem.html
            Our final solution, then, in O(nlogn)time, is as follows.
            First, sort the critical points. Then scan across the critical points from left to right.
            When we encounter the left edge of a rectangle,
            we add that rectangle to the heap with its height as the key.
            When we encounter the right edge of a rectangle, we remove that rectangle from the heap.
            (This requires keeping external pointers into the heap.)
            Finally, any time we encounter a critical point, after updating the heap we set the height of that critical
            point to the value peeked from the top of the heap.
        '''

        '''
            https://discuss.leetcode.com/topic/14987/108-ms-17-lines-body-explained
            This is a Python version of my modification of dong.wang.1694's brilliant C++ solution.
            It sweeps from left to right. But it doesn't only keep heights of "alive buildings" in the priority queue
            and it doesn't remove them as soon as their building is left behind.
            Instead, (height, right) pairs are kept in the priority queue and they stay in there
            as long as there's a larger height in there, not just until their building is left behind.

            In each loop, we first check what has the smaller x-coordinate: adding the next building from the input,
            or removing the next building from the queue. In case of a tie, adding buildings wins,
            as that guarantees correctness (think about it :-).
            We then either add all input buildings starting at that x-coordinate or
            we remove all queued buildings ending at that x-coordinate or earlier
            (remember we keep buildings in the queue as long as they're "under the roof"
            of a larger actually alive building). And then, if the current maximum height in the queue differs
            from the last in the skyline, we add it to the skyline.
        '''
        skyline = []
        i, n = 0, len(buildings)
        liveBd = []
        while i < n or liveBd:
            if not liveBd or i < n and buildings[i][0] <= -liveBd[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(liveBd, (-buildings[i][2], - buildings[i][1]))
                    i += 1
            else:
                x = - liveBd[0][1]
                while liveBd and -liveBd[0][1] <= x:
                    heappop(liveBd)
            height = len(liveBd) and - liveBd[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline












