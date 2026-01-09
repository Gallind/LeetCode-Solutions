class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def combRec(start: int, state):
            print(f"start - {start}\nstate - {state}")
            if len(state) == k:
                sol.append(list(state))
                return
            for i in range(start, n + 1):
                state.append(i)
                combRec(i + 1, state)
                state.pop()
        combRec(1, deque(list()))
        return sol