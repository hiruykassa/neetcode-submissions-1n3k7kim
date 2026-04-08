class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = len(prices) - 1
        res = []
        for l in range(len(prices)):
            if(prices[l] > prices[r] and r >= l):
                r -= 1
            
            if(prices[l] <= prices[r] and r >= l):
                result = prices[r] - prices[l]
                res.append(result)
                r -= 1

        max_res = max(res)
        return max_res




