class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, num in enumerate(strs):
            key = tuple(sorted(num))

            if key in seen:
                seen[key].append(num)

            else:
                seen[key] = [num]

        return list(seen.values())