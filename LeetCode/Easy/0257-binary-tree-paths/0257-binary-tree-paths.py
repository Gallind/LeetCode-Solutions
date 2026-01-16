# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        sol = []
        temp = []
        def backtrack(root):
            nonlocal sol
            nonlocal temp
            if not root: 
                return
            temp.append(str(root.val))
            if not root.left and not root.right:
                sol.append('->'.join(temp))
                temp.pop()
                return
            backtrack(root.left)
            backtrack(root.right)
            temp.pop()
        backtrack(root)
        return sol