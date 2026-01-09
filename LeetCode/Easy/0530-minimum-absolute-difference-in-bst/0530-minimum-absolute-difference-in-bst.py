import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minimum = math.inf
        if not root: return
        def setMin(root):
            if not root: return
            if not root.left and not root.right: return
            if root.left:
                def rightest(root):
                    if not root: return 0
                    if not root.right: return root.val
                    return rightest(root.right)
                closestVal = rightest(root.left)
                self.minimum = min(self.minimum, root.val - closestVal)
                setMin(root.left)
            if root.right:
                def leftest(root):
                    if not root: return 0
                    if not root.left: return root.val
                    return leftest(root.left)
                closestVal = leftest(root.right)
                self.minimum = min(self.minimum, closestVal - root.val)
                setMin(root.right)
        setMin(root)
        return self.minimum