import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    num = num & ((1 << 32) - 1)
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3:
                res |= 1 << i
        if res >= 1 << 31:
            res -= 1 << 32
        return res





        # max_num = max(nums)
        # bits = int(math.log2(max_num)) + 1
        # res = 0
        # for i in range(32):
        #     res <<= 1
        #     bit_sum = 0
        #     for j, num in enumerate(nums):
        #         bit_sum += num & 1
        #         nums[j] = num >> 1
        #     res |= bit_sum % 3
        # sol = 0
        # while res > 0:
        #     sol <<= 1
        #     sol |= res & 1
        #     res >>= 1
        # if sol >= (1 << 31):
        #     sol -= (1 << 32)
        # return sol

        