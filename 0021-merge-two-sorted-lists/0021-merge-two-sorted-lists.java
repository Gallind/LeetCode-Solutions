/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head1 = list1, head2 = list2;
        ListNode solHead = null;
        ListNode solTemp = solHead;
        if (head1 == null && head2 == null) return solHead;
        if (head1 == null) return head2;
        if (head2 == null) return head1;
        ListNode min;
        while (head1 != null && head2 != null){
            if (head1.val <= head2.val){
                min = new ListNode(head1.val);
                head1 = head1.next;
            }
            else{
                min = new ListNode(head2.val);
                head2 = head2.next;
            }
            if (solHead == null) {
                solHead = min;
                solTemp = solHead;
            }
            else{
                solTemp.next = min;
                solTemp = solTemp.next;
            }

        }
        if (head1 == null && head2 != null){
            solTemp.next = head2;
        }
        else if (head2 == null && head1 != null){
            solTemp.next = head1;
        }
        return solHead;
    }
}