class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_res = 0

        for price in prices:
            min_price = min(min_price, price)
            max_res = max(max_res, price - min_price)

        return max_res




