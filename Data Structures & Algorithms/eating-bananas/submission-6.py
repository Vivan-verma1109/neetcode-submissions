import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if 2 works so does 3 4 5....
        # still eneda check everything before 2
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
            
            