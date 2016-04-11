/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        //if(head==null) return head;
        ListNode preHead = new ListNode(0);
        preHead.next = head;
        ListNode pre = preHead, cur = head, next;
        while(cur != null) {
            boolean isDup = false;
            next = cur.next;
            while(next != null && next.val == cur.val) {
                isDup = true;
                next = next.next;
            }
            if(isDup){
                pre.next = next;
                cur = next;
            }else{
                pre = cur;
                cur = next;
            }
        }
        return preHead.next;
    }
}
