class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split(' ')
        if len(pattern) != len(s_lst): return False
        p_dict, s_dict = {}, {}
        for i, chs in enumerate(zip(pattern, s_lst)):
            ch, wrd = chs
            if ch not in p_dict: p_dict[ch] = i
            if wrd not in s_dict: s_dict[wrd] = i
            if p_dict[ch] != s_dict[wrd]: return False
        return True