# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_head = Node(head.val)

        node_map = {head: new_head}

        node = head.next
        prev = new_head

        while node:
            new_node = Node(node.val)
            prev.next = new_node
            node_map[node] = new_node
            prev = new_node
            node = node.next

        node = head
        prev = new_head
        while node:
            if node.random:
                prev.random = node_map[node.random]
            prev = prev.next
            node = node.next

        return new_head
