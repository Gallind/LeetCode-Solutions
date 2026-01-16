class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(1 + n * 8) - 1) / 2)