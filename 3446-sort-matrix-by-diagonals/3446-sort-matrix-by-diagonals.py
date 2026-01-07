class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        r_edge = n - 1
        amount_diag = n + r_edge
        diagonals = []
        upper_diagonals = []
 
        for i in range(n - 1):
            diag = []
            for row in range(n):
                hor_index = r_edge - i + row
                if hor_index <= r_edge:
                    diag.append(grid[row][hor_index])
            upper_diagonals.append(diag)
        for d in upper_diagonals:
            d.sort()
        lower_diagonals = []

        for i in range(n):
            diag = []
            for row in range(n):
                hor_index = row - r_edge + i
                if hor_index >= 0:
                    diag.append(grid[row][hor_index])
            lower_diagonals.append(diag)
        for d in lower_diagonals:
            d.sort(reverse=True)
        diagonals.extend(upper_diagonals)
        diagonals.extend(lower_diagonals[::-1])
        sol = []
        for i in range(n):
            rows = []
            for j in range(n):
                rows.append(diagonals[i - j + (n - 1)][min(i, j)])
            sol.append(rows)
        return sol
        