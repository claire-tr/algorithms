/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Palindrome_Linked_List_234 {

      //Definition for singly-linked list.
      public class ListNode {
          int val;
          ListNode next;
          ListNode(int x) { val = x; }
      }
        /*
         * Someone would argue that reverse the list is not considered as O(1) space, someone argues against it.
         * However, there seems to be no better solution, so we will still reverse first half of the list here
         * Note: 1. If the number of nodes in the linked list is odd
         *       2. Reversing the first half is more efficient than reversing the last half
         *       2. No, it's actually the same. Not even slightly different
         */
        public boolean isPalindrome(ListNode head) {
            if(head == null) return true;
            ListNode slow = head, fast = head;
            while(fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
            slow = reverse(slow);
            if(fast != null)

            return true;
        }

        private ListNode reverse(ListNode head) {
            ListNode next = null, pre = null;
            while(head != null) {
                pre = head.next;
                head.next = next;
                next = head;
                head = head.next;
            }
            return head;
        }
}
