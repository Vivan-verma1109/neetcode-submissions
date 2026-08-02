import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            midSpeed = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + midSpeed - 1) // midSpeed

            if hours <= h:
                right = midSpeed
            else:
                left = midSpeed + 1

        return left