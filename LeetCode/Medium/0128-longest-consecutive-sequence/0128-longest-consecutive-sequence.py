class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        max_len = 0
        for num in count:
            if num - 1 not in count:
                len_t = 1
                while num + len_t in count:
                    len_t += 1
                max_len = max(max_len, len_t)
        return max_len