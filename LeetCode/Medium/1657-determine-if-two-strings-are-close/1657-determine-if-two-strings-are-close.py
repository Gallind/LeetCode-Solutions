class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return ((freq1:=Counter(word1)).keys() == (freq2:=Counter(word2)).keys()) \
            and sorted(freq1.values()) == sorted(freq2.values())