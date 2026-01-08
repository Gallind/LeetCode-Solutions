class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([st for st in s.strip().split(' ') if len(st) > 0][::-1])
