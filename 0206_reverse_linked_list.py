# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """creates copy of linked list that is reversed"""
        current = None
        
        while head:
            current = ListNode(head.val, current)
            head = head.next
            
        return current

    def reverseListInPlace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """reverses linked list in place"""
        last = None
        current = head
        
        while current:
            next_node = current.next
            
            current.next = last
            
            last = current
            current = next_node
            
        return last
