# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Brute Force O(mn)

# Hash Map Time:O(m+n), Space O(m)

# Get the length of two list, let the longer one move the difference first

# This method, by switching heads, counter the possible difference of the length
# On the second round, they either hit, or reach the end(None) at the same time (no intersection)
# After second round, return headA.


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        # keep the two heads
        h1 = headA
        h2 = headB
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
            if headA == headB:
                return headA
            if not headA:
                headA = h2
            if not headB:
                headB = h1
        return headA
        
