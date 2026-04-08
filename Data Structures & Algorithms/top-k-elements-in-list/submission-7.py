class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap
        seen = {}
        # loop over nums
        for num in nums:
            # if num exists increment count
            if num in seen:
                seen[num] += 1
            # if not, initialize count
            else:
                seen[num] = 1

        newlist = []
        for i in range(k):
            most_frequent = max(seen, key=lambda x: seen[x])
            newlist.append(most_frequent)
            seen.pop(most_frequent)

        return newlist