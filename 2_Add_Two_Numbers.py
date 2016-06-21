# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Another solution: calculate the sum, while form a new linked list
        # See https://leetcode.com/discuss/2308/is-this-algorithm-optimal-or-what
        carry = 0
        preHead = ListNode(0)
        cur = preHead

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            next = ListNode(v1 + v2 + carry)
            if next.val > 9:
                next.val -= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            cur.next = next
            cur = next
        if carry != 0:
            next = ListNode(carry)
            cur.next = next

        return preHead.next

