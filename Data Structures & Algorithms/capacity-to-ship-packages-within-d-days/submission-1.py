class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            weight = (l + r) // 2

            total = 0
            days_taken = 1
            for i in weights:
                total += i
                if total > weight:
                    days_taken += 1
                    total = i
            
            if days_taken > days:
                l = weight + 1
            else:
                r = weight - 1
        return l