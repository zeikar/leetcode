# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        head = ListNode()
        pr, r = None, head
        carry = 0

        while p1 != None or p2 != None:
            v1, v2 = 0, 0
            if p1 != None:
                v1 = p1.val
                p1 = p1.next
            if p2 != None:
                v2 = p2.val
                p2 = p2.next

            r.val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10

            pr = r
            r.next = ListNode()
            r = r.next

        if carry != 0:
            r.val = 1
        else:
            pr.next = None

        return head
