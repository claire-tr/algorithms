/**
 * Created by YunyunChen1 on 4/18/16.
 */
public class Reverse_Linked_List_206 {
    /*
     * pre -> previous node
     * next -> next node
     * move these two nodes after pointed
     *
     */
    public class ListNode {
             int val;
             ListNode next;
             ListNode(int x) { val = x; }
         }

    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        while(head != null) {
            ListNode next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }
}
