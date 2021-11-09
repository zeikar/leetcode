from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.mergeTwoLists(lists, 0, len(lists) - 1)
        if len(lists) == 0:
            return None
        return lists[0]

    def mergeTwoLists(self, lists: List[Optional[ListNode]], left: int, right: int) -> None:
        if left >= right:
            return None

        mid = (left + right) // 2
        self.mergeTwoLists(lists, left, mid)
        self.mergeTwoLists(lists, mid + 1, right)

        self.merge(lists, left, mid + 1)
        return None

    def merge(self, lists: List[Optional[ListNode]], left: int, right: int) -> None:
        left_cur = lists[left]
        right_cur = lists[right]
        head = ListNode()
        cur = head

        while left_cur and right_cur:
            if left_cur.val < right_cur.val:
                cur.next = left_cur
                left_cur = left_cur.next
            else:
                cur.next = right_cur
                right_cur = right_cur.next

            cur = cur.next

        if left_cur:
            cur.next = left_cur

        if right_cur:
            cur.next = right_cur

        lists[left] = head.next
