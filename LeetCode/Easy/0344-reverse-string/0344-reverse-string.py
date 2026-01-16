class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(l:=len(s)):
            if i >= l - 1 - i: break
            s[i], s[l - 1 - i] = s[l - 1 - i], s[i]
            