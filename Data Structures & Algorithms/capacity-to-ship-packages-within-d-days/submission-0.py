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
            print(days_taken, weight)

            if days_taken <= days:
                r = weight
            else:
                l = weight + 1
        return l

