class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        if len(nums) == 0: return -1
        if nums[0] == total: return 0
        l_sum = 0
        for i, n in enumerate(nums):
            if l_sum == total - l_sum - n: return i
            l_sum += n
        return -1
        