# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MAX_D = -1
    def diameter(self, root: Optional[TreeNode]):
        if not root: return 0
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        self.MAX_D = max(self.MAX_D, left + right)
        return max(left, right) + 1
           
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter(root)
        return self.MAX_D