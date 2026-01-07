class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # start = 0
        # # end = len(nums) - 1
        # end = 0

        l = 0
        # i = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[l] = n
                if l < i:
                    nums[i] = 0
                l += 1
        for i in range(l + 1, len(nums)):
            nums[i] = 0

        # while start <= end:
        #     while end < len(nums) and nums[end] != 0:
        #         end += 1
        #     if nums[start] == 0:
        #         nums[start], nums[end] = nums[end], nums[start]
        #     start += 1

        # while start < end:
        #     if nums[start] == 0:
        #         nums[start], nums[end] = nums[start + 1], nums[start]
        #         end -= 1
        #     else:
        #         start += 1
        
        