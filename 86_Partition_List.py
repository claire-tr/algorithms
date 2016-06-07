# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # use two new head to store two kinds of nodes separately
        # connect the two lists

        p1 = cur1 = ListNode(0)
        p2 = cur2 = ListNode(0)

        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next

        cur1.next = p2.next
        cur2.next = None

        return p1.next