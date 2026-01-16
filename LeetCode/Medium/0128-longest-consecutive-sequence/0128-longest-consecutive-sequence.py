class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        for num in (nums_set:=set(nums)):
            if num - 1 not in nums_set:
                len_t = 1
                while num + len_t in nums_set:
                    len_t += 1
                max_len = max(max_len, len_t)
        return max_len