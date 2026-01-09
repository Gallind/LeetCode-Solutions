# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def pathSumRec(root, currSum, targetSum):
            if not root:
                return False
            currSum += root.val
            if not root.left and not root.right:
                return currSum == targetSum
            return pathSumRec(root.left, currSum, targetSum) or pathSumRec(root.right, currSum, targetSum)
        return pathSumRec(root, 0, targetSum)
        