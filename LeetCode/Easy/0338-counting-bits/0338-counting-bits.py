import math
class Solution:
    def countBits(self, n: int) -> List[int]:
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