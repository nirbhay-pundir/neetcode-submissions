class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_count = {}
        for i in range(len(s)):
            if s[i] in ch_count.keys():
                ch_count[s[i]] += 1
            else:
                ch_count[s[i]] = 1
            if t[i] in ch_count:
                ch_count[t[i]] -= 1
            else:
                ch_count[t[i]] = -1

        for v in ch_count.values():
            if v != 0:
                return False
        return True