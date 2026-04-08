class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = "".join([c for c in s if c.isalpha()])
        newT = "".join([d for d in t if d.isalpha()])
        return sorted(newS.lower()) == sorted(newT.lower())
        