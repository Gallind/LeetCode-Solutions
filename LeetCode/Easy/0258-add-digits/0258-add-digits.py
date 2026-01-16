class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        total = 0
        temp = num
        while temp > 0:
            total += temp % 10
            temp //= 10
        return self.addDigits(total)