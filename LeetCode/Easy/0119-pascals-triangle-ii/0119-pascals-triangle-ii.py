class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        solTemp = [[0, 1, 0]]
        for i in range(0, rowIndex):
            row = [0]
            for j in range(len(sT:=solTemp[-1]) - 1):
                row.append(sT[j] + sT[j+1])
            row.append(0)
            solTemp.append(row)
        return solTemp[-1][1:-1]