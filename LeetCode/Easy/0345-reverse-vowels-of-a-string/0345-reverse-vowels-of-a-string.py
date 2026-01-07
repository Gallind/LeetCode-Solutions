class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s_list = list(s)
        start = 0
        end = len(s_list) - 1
        while start < end:
            while start < end and s_list[start] not in vowels:
                start += 1
            while start < end and s_list[end] not in vowels:
                end -= 1
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
        return "".join(s_list)

        # vowel_word = ""
        # vowel_indices = []
        # for i, ch in enumerate(s):
        #     if ch in vowels:
        #         vowel_word += ch
        #         vowel_indices.append(i)
        # vowel_word = vowel_word[::-1]
        # for i, index in enumerate(vowel_indices):
        #     if index == 0:
        #         s = vowel_word[i] + s[1:]
        #     elif index == len(s) - 1:
        #         s = s[:-1] + vowel_word[i]
        #     else:
        #         s = s[:index] + vowel_word[i] + s[index + 1:]
        # return s