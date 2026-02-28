class Solution:
    def concatenatedBinary(self, n: int) -> int:
        m = 10**9 + 7
        sol = 0
        bits = 0

        for i in range(1, n + 1):
            if not (i & (i - 1)):
                bits += 1
            sol = ((sol << bits) | i) % m
        
        return sol