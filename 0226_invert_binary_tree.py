# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/invert-binary-tree/
class Solution:
    # inplace iteritive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                stack.append(current.right)
                stack.append(current.left)
                current.left, current.right = current.right, current.left
        return root
        
    # one liner recursive, original tree is not effected.
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
