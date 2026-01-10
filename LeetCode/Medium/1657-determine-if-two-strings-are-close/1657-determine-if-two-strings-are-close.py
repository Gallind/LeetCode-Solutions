class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c1, c2 in zip(word1, word2):
            freq1[ord(c1) - ord('a')] += 1
            freq2[ord(c2) - ord('a')] += 1
        for f1, f2 in zip(freq1, freq2):
            if (f1 and not f2) or (f2 and not f1): return False
        freq1.sort()
        freq2.sort()
        return freq1 == freq2