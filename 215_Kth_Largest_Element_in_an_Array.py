import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # min heap
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap, n)
        for _ in xrange(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)