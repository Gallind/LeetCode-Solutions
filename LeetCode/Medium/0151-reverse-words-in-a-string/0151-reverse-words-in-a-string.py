class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.strip().split(' ')
        lst2 = [st for st in lst if len(st) > 0]
        lst3 = lst2[::-1]
        return " ".join(lst3)