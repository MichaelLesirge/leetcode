# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# not my best work
class Solution:
    def __init__(self):
        self.memo = {None: 0}
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return abs(self.findHeight(root.left) - self.findHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
                
    
    def findHeight(self, root: Optional[TreeNode]) -> int:
        if root not in self.memo:
            self.memo[root] = max(self.findHeight(root.left), self.findHeight(root.right)) + 1
        return self.memo[root]
    
