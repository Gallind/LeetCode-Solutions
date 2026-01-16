class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i, ch in enumerate(s):
            if ch not in dict_s:
                dict_s[ch] = {i,}
            else:
                dict_s[ch].add(i)
        for i, ch in enumerate(t):
            if ch not in dict_t:
                dict_t[ch] = {i,}
            else:
                dict_t[ch].add(i)
        print(f"{dict_s = }\n{dict_t = }")
        print(f"\n\n{list(dict_s.values()) = }\n{list(dict_t.values()) = }")
        return all(s1 == s2 for s1, s2 in zip(list(dict_s.values()), list(dict_t.values())))
        # return dict_s.values() == dict_t.values()