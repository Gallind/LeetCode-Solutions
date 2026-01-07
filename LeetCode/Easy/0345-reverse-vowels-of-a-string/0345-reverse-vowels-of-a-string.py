class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_word = ""
        vowel_indices = []
        for i, ch in enumerate(s):
            if ch in vowels:
                vowel_word += ch
                vowel_indices.append(i)
        vowel_word = vowel_word[::-1]
        for i, index in enumerate(vowel_indices):
            if index == 0:
                s = vowel_word[i] + s[1:]
            elif index == len(s) - 1:
                s = s[:-1] + vowel_word[i]
            else:
                s = s[:index] + vowel_word[i] + s[index + 1:]
        return s