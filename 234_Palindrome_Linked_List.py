# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 合理设计函数,注意可复用性
# 不要只想着这个程序能跑成功,还要想这样写到底是不是合理的,以后改是不是好改的,
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        mid = self.getMid(head)
        right = mid.next
        mid.next = None
        return self.compare(head, self.rotate(right))

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def rotate(self, head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def compare(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True
