class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        if n <= 0: return False
        if not n % 2: return self.isUgly(n >> 1)
        if not n % 3: return self.isUgly(n // 3)
        if not n % 5: return self.isUgly(n // 5)
        return False