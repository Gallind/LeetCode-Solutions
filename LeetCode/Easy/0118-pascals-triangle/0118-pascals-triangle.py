class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = []
        if not numRows: return []
        solTemp = [[0, 1, 0]]
        for i in range(numRows - 1):
            row = [0]
            for j in range(len((sT:=solTemp[-1])) - 1):
                row.append(sT[j] + sT[j+1])
            row.append(0)
            solTemp.append(row)
        for s in solTemp:
            sol.append(s[1:-1])
        return sol