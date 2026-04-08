class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        while len(s) == len(t):
            sortedS = sorted(s)
            sortedT = sorted(t)
            return sortedS == sortedT
        return False        