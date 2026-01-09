/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = 0, lenB = 0;
        ListNode a = headA;
        ListNode b = headB;
        while (a != null){
            lenA++;
            a = a.next;
        }
        while (b != null){
            lenB++;
            b = b.next;
        }
        // System.out.println("a - " + lenA + "\nb - " + lenB);
        int diff = Math.abs(lenA - lenB);
        a = headA; 
        b = headB;
        if (lenA > lenB){
            for (int i = 0; i < diff; i++) a = a.next;
        }
        else{
            for (int i = 0; i < diff; i++) b = b.next;
        }
        while (a != null){
            if (a == b) return a;
            a = a.next;
            b = b.next;
        }
        return null;
    }
}