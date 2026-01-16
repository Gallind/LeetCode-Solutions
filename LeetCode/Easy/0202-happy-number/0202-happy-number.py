class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        if n <= 4: return False
        sum_digits = 0
        temp = n
        while temp > 0:
            sum_digits += (temp % 10) ** 2
            temp //= 10
        print(sum_digits)
        return self.isHappy(sum_digits)