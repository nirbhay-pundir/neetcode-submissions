class Solution:

    def encode(self, strs: List[str]) -> str:
        return "~".join(strs) if len(strs) > 0 else "NONE"

    def decode(self, s: str) -> List[str]:
        return s.split("~") if s != "NONE" else []