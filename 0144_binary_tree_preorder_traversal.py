# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        nodes = []

        while stack:
            current = stack.pop()

            if current is None: continue

            nodes.append(current.val)
            stack.append(current.right)
            stack.append(current.left)

        return nodes
