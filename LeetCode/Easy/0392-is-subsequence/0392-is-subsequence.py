class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls > lt: return False
        if not s and not t: return True

        left = right = 0
        end = lt - 1
        while right <= end:
            if left >= ls: return True
            if s[left] == t[right]:
                if left == ls - 1: return True
                left += 1
                right += 1
            else:
                right += 1
        return False
        