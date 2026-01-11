class Solution:
    def sumZero(self, n: int) -> List[int]:
        half = n // 2
        sol = [i for i in range(0 - half, half + 1)]
        if not n % 2:
            return sol[:half - 1] + sol[half:]
        return sol