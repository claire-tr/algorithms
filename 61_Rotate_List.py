# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        preHead = ListNode(0)
        preHead.next = head
        fast = slow = head

        length = self.getLen(head)
        k %= length

        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = preHead.next
        newHead = slow.next
        slow.next = None
        return newHead

    def getLen(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
