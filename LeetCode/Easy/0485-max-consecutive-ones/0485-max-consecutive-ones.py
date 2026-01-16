class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        cons1 = 0
        for n in nums:
            if n: 
                cons1 += 1
                max1 = max(max1, cons1)
            else:
                cons1 = 0
        return max1