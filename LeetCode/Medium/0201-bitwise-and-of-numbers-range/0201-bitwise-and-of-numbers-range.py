class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1
        return right

        # if right >= left << 1: return 0
        # total = 0
        # for i in range(32):
        #     bit = 1
        #     for num in range(left, right + 1):
        #         bit &= (num >> i) & 1
        #         if not bit: break
        #     total |= bit << i
        # return total
