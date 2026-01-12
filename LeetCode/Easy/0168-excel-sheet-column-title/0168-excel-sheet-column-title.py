class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        sol = ""
        while columnNumber > 0:
            columnNumber -= 1
            let = columnNumber % 26
            columnNumber //= 26
            sol += chr(let + ord('A'))
        return sol[::-1]
