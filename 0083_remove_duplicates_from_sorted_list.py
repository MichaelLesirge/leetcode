# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        go though each value
        everytime we see new number save it
        connect it to new number when found
        connect to none at end
        """
        if head is None: return head

        cur = first_of_type = head
        while cur:
            if first_of_type.val != cur.val:
                first_of_type.next = cur
                first_of_type = cur
            cur = cur.next
        first_of_type.next = None
        return head

