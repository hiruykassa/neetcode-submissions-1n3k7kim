class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1 

            key = tuple(count)
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]

        return list(seen.values())

            
