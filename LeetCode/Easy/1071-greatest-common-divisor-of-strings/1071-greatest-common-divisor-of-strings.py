import math
class Solution:
    # def isDiv(self, s: str, sub: str):
    #     if not s: return True
    #     if s.find(sub) != 0: return False
    #     return self.isDiv(s[len(sub):], sub)
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = str1 + str2
        s2 = str2 + str1
        if s1 != s2:
            return ""
        gcd = math.gcd(len(str1), len(str2))
        return str1[:gcd]
        # max_div = ""
        # prefix = ""
        # for ch in str1:
        #     prefix += ch
        #     if self.isDiv(str1, prefix) and self.isDiv(str2, prefix):
        #         max_div = prefix
        # return max_div
        