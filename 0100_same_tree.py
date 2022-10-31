# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTreeNormal(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p is q:           
                continue
            if not ((p and q) and (p.val == q.val)):
                return False
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True
    
    # overly complex one-liner    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (p is q) or ((p and q) and (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
