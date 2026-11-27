class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_length = 0
        l = 0

        for r, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1
            last_seen[ch] = r
            length = r - l + 1
            if length > max_length:
                max_length = length

        return max_length