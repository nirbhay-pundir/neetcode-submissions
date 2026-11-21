class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_ch_count = {}
        t_ch_count = {}
        for i in range(len(s)):
            if s[i] in s_ch_count.keys():
                s_ch_count[s[i]] += 1
            else:
                s_ch_count[s[i]] = 1
            if t[i] in t_ch_count:
                t_ch_count[t[i]] += 1
            else:
                t_ch_count[t[i]] = 1
        if len(s_ch_count) != len(t_ch_count):
            return False
        for ch in s_ch_count.keys():
            try:
                if s_ch_count[ch] != t_ch_count[ch]:
                    return False
            except(KeyError):
                return False
        return True