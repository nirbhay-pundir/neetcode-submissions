class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch for ch in s.lower() if ch.isalnum())
        return cleaned == cleaned[::-1]