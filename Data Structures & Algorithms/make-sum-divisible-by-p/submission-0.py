class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if sum(nums) % p == 0:
            return 0
        
        remainder = {0: -1}
        curSum = 0
        best = float("inf")
        for idx, num in enumerate(nums):
            curSum += num
            curRem = (curSum) % p
            needRem = (curRem - target) % p
            if needRem in remainder:
                best = min(idx - remainder[needRem], best)
            remainder[curRem] = idx
        return best if best < len(nums) else -1

            
