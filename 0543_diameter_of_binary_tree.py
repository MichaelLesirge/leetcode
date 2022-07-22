# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
    
        def diameterOfNode(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left, right = diameterOfNode(root.left), diameterOfNode(root.right)
            # self.max_diameter = max(self.max_diameter, left+right)
            lr_sum = left+right
            if lr_sum > self.max_diameter:
                self.max_diameter = lr_sum
            return max(left, right) + 1
        
        
        diameterOfNode(root)
        return self.max_diameter
