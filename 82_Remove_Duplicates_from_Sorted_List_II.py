# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        preHead = ListNode(0)
        preHead.next = head
        pre, cur = preHead, head

        while cur and cur.next:
            nextN = cur.next
            if nextN.val == cur.val:
                while nextN and cur.val == nextN.val:
                    pre.next = nextN.next
                    nextN = nextN.next
                cur = nextN
            else:
                pre = cur
                cur = cur.next
        return preHead.next