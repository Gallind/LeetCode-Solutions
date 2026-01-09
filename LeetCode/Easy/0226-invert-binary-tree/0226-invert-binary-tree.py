# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return 
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
        # dup = TreeNode()
        # def revertT(root, dup):
        #     if not root: return
        #     dup.val = root.val
        #     if not root.left and not root.right: return
        #     if root.left:
        #         dup.right = TreeNode()
        #         revertT(root.left, dup.right)
        #     if root.right:
        #         dup.left = TreeNode()
        #         revertT(root.right, dup.left)
        # revertT(root, dup)
        # return dup