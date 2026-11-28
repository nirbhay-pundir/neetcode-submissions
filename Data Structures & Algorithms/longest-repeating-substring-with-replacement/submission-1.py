class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_count = {}
        max_freq = 0
        l = 0

        for r, ch in enumerate(s):
            ch_count[ch] = ch_count.get(ch, 0) + 1
            if ch_count[ch] > max_freq:
                max_freq = ch_count[ch]
            if (r - l + 1) - max_freq > k:
                ch_count[s[l]] -= 1
                l += 1

        return len(s) - l