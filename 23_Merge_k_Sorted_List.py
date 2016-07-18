class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        '''
            store the (node.val, node) pair in heap
            # avoid changing heap size
            https://discuss.leetcode.com/topic/23140/108ms-python-solution-with-heapq-and-avoid-changing-heap-size/2
        '''
        import heapq
        val = []
        preHead = cur = ListNode(-1)
        for node in lists:
            if node:
                val.append((node.val, node))
        heapq.heapify(val)
        while val:
            v, n = heapq.heappop(val)
            cur.next = ListNode(v)
            if n.next:
                heapq.heappush(val, (n.next.val, n.next))
            cur = cur.next
        return preHead.next
