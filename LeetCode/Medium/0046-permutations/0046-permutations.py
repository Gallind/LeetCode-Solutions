class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        sol = []

        def permRec(state):
            if len(state) == l:
                sol.append(state[:])
                return
            
            for n in nums:
                if n not in state:
                    state.append(n)
                    permRec(state)
                    state.pop()

        permRec([])
        return sol