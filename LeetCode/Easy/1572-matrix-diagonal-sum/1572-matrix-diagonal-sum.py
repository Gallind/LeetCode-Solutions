class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        l = len(mat)
        for i in range(l):
            total += mat[i][i]
            total += mat[i][l - 1 - i]
        if l & 1:
            total -= mat[l // 2][l // 2]
        return total