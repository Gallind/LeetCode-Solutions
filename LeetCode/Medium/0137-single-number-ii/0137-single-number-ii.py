import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    num = num & ((1 << 32) - 1)
                bit_sum += (num >> i) & 1
                # if (num >> i) & 1:
                #     bit_sum += 1
            # res |= (bit_sum % 3) << i
            if bit_sum % 3:
                res |= 1 << i
        if res >= 1 << 31:
            res -= 1 << 32
        return res
