class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        length = len(s_lower)
        i = 0
        j = length - 1
        while i < (length // 2):
            if not s_lower[i].isalnum():
                i += 1
                continue
            if not s_lower[j].isalnum():
                j -= 1
                continue
                
            if s_lower[i] != s_lower[j]:
                return False
            i += 1
            j -= 1
        return True