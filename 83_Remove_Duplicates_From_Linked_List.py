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
        if not head:
            return head
        pre = head
        cur = head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return head

