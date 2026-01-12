class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2: return 2
        if n == 1: return 1
        if not n: return 0
        steps = [0] * n
        steps[0], steps[1], steps[2] = 0, 1, 2
        for i in range(3, n):
            steps[i] = steps[i-2] + steps[i-1]
        return steps[n-1] + steps[n-2]

        