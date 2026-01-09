# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.totals = []
        def sumLevel(root=root, h=0):
            if not root: return
            if len(self.totals) == h:
                self.totals.append([root.val,1])
            else:
                self.totals[h][0] += root.val
                self.totals[h][1] += 1
            h += 1
            sumLevel(root.left, h)
            sumLevel(root.right, h)
        sumLevel()
        res = [total / count for total, count in self.totals]
        return res

        