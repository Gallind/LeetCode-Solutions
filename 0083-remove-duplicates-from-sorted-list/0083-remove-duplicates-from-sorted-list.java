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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;
        ListNode headTemp = head;
        int tempVal = headTemp.val;
        while (headTemp.next != null){
            if (tempVal < headTemp.next.val){
                headTemp = headTemp.next;
                tempVal = headTemp.val;
            }
            else{
                headTemp.next = headTemp.next.next;
            }
        }
        return head;
    }
}