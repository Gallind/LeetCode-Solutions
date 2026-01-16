class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_note = Counter(ransomNote)
        freq_mag = Counter(magazine)
        for ch in freq_note.keys():
            if freq_mag[ch] < freq_note[ch]: 
                return False
        return True