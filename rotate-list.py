# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if k % length == 0:
            return head

        # rotate
        curr = head
        for _ in range(length - k % length - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None

        # connect
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head

        return new_head
