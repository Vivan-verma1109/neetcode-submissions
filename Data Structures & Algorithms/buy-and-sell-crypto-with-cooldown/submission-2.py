class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        sold = 0
        hold = float("-inf")

        for num in prices:
            holdval = max(hold, free - num)
            soldval = hold + num
            freeval = max(free, sold)

            hold = holdval
            sold = soldval
            free = freeval
        
        return max(free, sold, hold + num)
