class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == n == 1: return [1]
        if k >= n: return []
        sol = []

        def combRec(start, preSum, lst):
            if len(lst) == k and preSum == n:
                sol.append(lst[:])
                return
            for i in range(start, 10):
                if preSum + i > n: break

                lst.append(i)
                combRec(i + 1, preSum + i, lst)
                lst.pop()
        
        combRec(1, 0, [])
        return sol

        