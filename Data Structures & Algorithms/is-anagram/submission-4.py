class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ch_count = {}
        for c1, c2 in zip(s, t):
            ch_count[c1] = ch_count.get(c1, 0) + 1
            ch_count[c2] = ch_count.get(c2, 0) - 1

        return all(v == 0 for v in ch_count.values())