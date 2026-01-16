class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i, chs in enumerate(zip(s, t)):
            ch1, ch2 = chs
            if ch1 not in dict_s:
                dict_s[ch1] = {i,}
            else:
                dict_s[ch1].add(i)
            if ch2 not in dict_t:
                dict_t[ch2] = {i,}
            else:
                dict_t[ch2].add(i)
        return all(s1 == s2 for s1, s2 in zip(list(dict_s.values()), list(dict_t.values())))
