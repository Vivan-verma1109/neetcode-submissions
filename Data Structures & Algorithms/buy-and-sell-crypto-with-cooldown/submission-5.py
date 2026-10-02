class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        hold = float("-inf")
        sold = 0

        for num in prices:
            freeval = max(free, sold)
            holdval = max(hold, free - num)
            soldval = hold + num

            hold = holdval
            sold = soldval
            free = freeval

        return max(free, sold)