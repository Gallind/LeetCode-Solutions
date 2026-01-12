class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maxSum = nums[0]
        index = 0
        currSum = maxSum
        for num in nums[1:]:
            if num > currSum + num: currSum = num
            else: currSum += num
            if currSum > maxSum: maxSum = currSum
        return maxSum