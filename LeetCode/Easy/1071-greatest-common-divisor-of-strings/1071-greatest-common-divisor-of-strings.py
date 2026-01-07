class Solution:
    def isDiv(self, s: str, sub: str):
        if not s: return True
        if s.find(sub) != 0: return False
        return self.isDiv(s[len(sub):], sub)
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ""
        if str1.find(str2[0]) < 0 or str2.find(str1[0]) < 0:
            return ""
        max_div = ""
        prefix = ""
        for ch in str1:
            prefix += ch
            if self.isDiv(str1, prefix) and self.isDiv(str2, prefix):
                max_div = prefix
        return max_div
        