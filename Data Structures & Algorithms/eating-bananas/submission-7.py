class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            rate = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / rate)
            if hours <= h:
                r = rate
            else:
                l = rate + 1
        return l