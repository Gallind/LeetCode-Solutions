from functools import cache
class Solution:
    def countBits(self, n: int) -> List[int]:
        # @cache
        # def bits(x: int):
        #     if x == 0: return 0
        #     return bits(x >> 1) + (x & 1)
        
        # return [bits(i) for i in range(n + 1)]
        
        if n == 0: return [0]
        sol = [-1] * (n + 1)
        sol[0] = 0
        sol[1] = 1

        for i in range(1, n + 1):
            if sol[i] < 0:
                if i % 2 == 0:
                    sol[i] = sol[i // 2]
                else:
                    sol[i] = sol[i // 2] + 1
        return sol