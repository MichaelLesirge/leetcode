# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindromeFirst(self, head: Optional[ListNode]) -> bool:
        """
        store in array
        check first half of array agenst second half
        
        First thing i came up with.
        """
        array = []
        
        while head:
            array.append(head.val)
            head = head.next   
        
        # return array == array[::-1]
        for i in range(len(array)//2):
            if array[i] != array[-i-1]:
                return False
        return True

    
    #Follow up: Could you do it in O(n) time and O(1) space?
    def isPalindromeFollowUp(self, head: Optional[ListNode]) -> bool:
        """
        first half == reversed second half
        
        go though and find len
        go though first half
        go though second half and set next to last
        compare each nodes
        
        This solution is bad, but now I know about the fast/slow technique!
        """
        
        # find len
        current = head
        ll_len = 0
        while current:
            current = current.next
            ll_len += 1 # 0.5
        ll_half_len = ll_len // 2
        
        # get to midpoint
        current = head
        for _ in range(ll_half_len):
            print(current.val)
            current = current.next
        
        # skip middle if odd size
        if ll_len % 2 == 1:
            current = current.next
        
        # reverse second half
        last = None
        for _ in range(ll_half_len):
            next_node = current.next
            current.next = last
            last = current
            current = next_node
        
        # compare
        current = head
        for _ in range(ll_half_len):
            if current.val != last.val:
                return False
            current = current.next
            last = last.next
        
        return True
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Implementying fast/slow solution without looking at other peoples code.
        """
        fast = slow = head
        last = None
        # slow only gets half way becuase fast reaches end x2 faster
        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next
            slow.next = last
            last = slow
            slow = next_slow
            
            
        # if fast lands on None that means the linked list has a even number of nodes
        if fast:
            slow = slow.next
        
        # since we only reverse the first half we end up with "last" at the start of the reversed half
        # and since slow is set to the next node before the reversal it is and the start of the second half
        while slow:
            if last.val != slow.val:
                return False
            last = last.next
            slow = slow.next
        
        return True
        
        
