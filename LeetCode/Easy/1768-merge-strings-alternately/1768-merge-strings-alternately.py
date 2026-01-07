class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        
        sol2 = []
        for c1, c2 in zip(word1, word2):
            sol2.append(c1 + c2)
        sol2.append(word1[l2:])
        sol2.append(word2[l1:])
        return "".join(sol2)

        # sol = ""
        # if l1 <= l2:
        #     for c1, c2 in zip(word1, word2[:l1]):
        #         sol += c1 + c2
        #     sol += word2[l1:]
        # else:
        #     for c1, c2 in zip(word1[:l2], word2):
        #         sol += c1 + c2
        #     sol += word1[l2:]
        # return sol
        