# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sol = dummy
        local_sum = c = 0
        while l1 or l2 or c:
            if l1 and l2:
                local_sum = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
            elif l1:
                local_sum = l1.val + c
                l1 = l1.next
            elif l2:
                local_sum = l2.val + c
                l2 = l2.next
            else: local_sum = c
            c = local_sum // 10
            dummy.next = ListNode(val=local_sum%10)
            dummy = dummy.next
        return sol.next
        