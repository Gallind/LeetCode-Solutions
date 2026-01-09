class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []

        def sumRec(index, state, total):
            if total == target: 
                sol.append(state[:])
                return
            if total > target: return
            for i in range(index, len(candidates)):
                state.append(candidates[i])
                sumRec(i, state, total + candidates[i])
                state.pop()
        sumRec(0, [], 0)
        return sol