class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[i] > prices [j]):
                    seen.append(0)
                else:
                    result = prices[j] - prices[i]
                    seen.append(result)
        max_diff = max(seen)
        return max_diff

