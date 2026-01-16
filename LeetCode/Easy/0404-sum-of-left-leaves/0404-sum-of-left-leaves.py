# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        def sumLL(root):
            nonlocal total
            if not root: return
            if root.left:
                if not root.left.left and not root.left.right: 
                    total += root.left.val
                sumLL(root.left)
            if root.right: sumLL(root.right)
        sumLL(root)
        return total
                