class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            for j in seen:
                if j == target - num:
                    return [seen[j], i]
            seen[num] = i
                

      

            