# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        dummy_head = ListNode()
        current = dummy_head
        
        carry = 0
        while l1 or l2 or carry:
            node_sum = carry
            if l1:
                node_sum += l1.val
                l1 = l1.next
            if l2:
                node_sum += l2.val
                l2 = l2.next
                
            carry = 0
            if node_sum > 9:
                carry=1
                node_sum -= 10
            current.next = ListNode(node_sum)
    
            current = current.next
        
        return dummy_head.next
    

    
# im going to leave in my plan out of the way at the bottom now
# they are not writen very well
"""
create head
carry = 0

while l1 or l2 or carry

sum = l1 if l1  +  l2 if l2 + carry
carry=0

if sum is greater then 10: carry = 1, sum -= 10
append node(sum)

"""
