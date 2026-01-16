class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = []
        seen = [i for i in range(0, n + 1)]
        for num in nums:
            seen[num] = 0
        for i in seen:
            if i: sol.append(i)
        return sol