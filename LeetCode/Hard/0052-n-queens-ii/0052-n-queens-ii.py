class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.table = [-1] * n
        def isSafe(col, row) -> bool:
            for c in range(col):
                if self.table[c] == row: return False
                if abs(self.table[c] - row) == abs(col - c): return False
            return True

        def solve(col):
            if col == n: 
                self.count += 1
                return
            for row in range(n):
                if isSafe(col, row):
                    self.table[col] = row
                    solve(col + 1)

        solve(0)
        return self.count