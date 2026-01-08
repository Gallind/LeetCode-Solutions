import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = len(nums)
        if k >= l: return sum(nums) / l
        max_sum = sum(nums[:k])
        curr_sum = max_sum
        for i in range(l - k):
            curr_sum += nums[i + k] - nums[i]
            if curr_sum > max_sum: max_sum = curr_sum
        return max_sum / k