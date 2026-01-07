class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[l] = n
                if l < i:
                    nums[i] = 0
                l += 1
        for i in range(l + 1, len(nums)):
            nums[i] = 0
        