class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = []
        seen = [0] * n
        for num in nums:
            seen[num - 1] = 1
        for i, see in enumerate(seen):
            if not see:
                sol.append(i + 1)
        return sol