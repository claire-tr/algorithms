/**
 * Created by YunyunChen1 on 4/18/16.
 */
public class Reverse_Linked_List_II_92 {
    public class ListNode {
             int val;
             ListNode next;
             ListNode(int x) { val = x; }
         }
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) return head;
        ListNode pre = null, start = null, last = null, preHead = new ListNode(-1);
        preHead.next = head;
        for (int i = 1; head != null; i++) {
            if (i == m-1)  {
                pre = head;
                start = head.next;
            }
            if (i == n) last = head.next;
            head = head.next;
        }
        pre.next = reverse(start, n-m, last);
        return preHead.next;
    }

    private ListNode reverse(ListNode head, int steps, ListNode last) {
        ListNode pre = last;
        while(steps>=0) {
            ListNode next = head.next;
            head.next = pre;
            pre = head;
            head = next;
            steps--;
        }
        return pre;
    }
}
