class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        sale = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                sale = max(sale, prices[i] - prices[l])
        return sale