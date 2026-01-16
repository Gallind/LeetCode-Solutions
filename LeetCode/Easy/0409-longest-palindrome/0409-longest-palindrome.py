class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        total = 0
        flag = True
        for val in freq.values():
            if flag and val % 2:
                flag = False
                total += val
                continue
            if val % 2: total += val - 1
            else: total += val
        return total