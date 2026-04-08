class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1

            else:
                seen[num] = 1

        k_freq = []
        for i in range(k):
            most_freq = max(seen, key=lambda x: seen[x])
            k_freq.append(most_freq)
            seen.pop(most_freq)

        return k_freq