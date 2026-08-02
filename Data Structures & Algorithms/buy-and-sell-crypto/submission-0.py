class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        sale = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                sale = max(sale, prices[r] - prices[l])
        return sale