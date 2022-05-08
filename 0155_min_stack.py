# https://leetcode.com/problems/min-stack/

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

class MinStack:
    """
    using singlaly linked list
    """
    def __init__(self):
        self.head = ListNode()

    def push(self, val: int) -> None:
        self.head.next_node = ListNode(val, self.head.next_node)
        
        
    def pop(self) -> None:
        old = self.head.next_node
        self.head.next_node = old.next_node
        return old.val

    def top(self) -> int:
        return self.head.next_node.val

    def getMin(self) -> int:
        current = self.head.next_node
        min_val = float("inf")
        while current:
            if min_val > current.val:
                min_val = current.val
            current = current.next_node
        return min_val
