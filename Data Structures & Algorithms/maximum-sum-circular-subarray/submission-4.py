class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        small = float("inf")
        big = float("-inf")
        cur = 0
        otherCur = 0

        for i in range(len(nums)):
            cur += nums[i]
            otherCur += nums[i]
            small = min(small, cur)
            big = max(big, otherCur)
            if cur > 0:
                cur = 0
            if otherCur < 0:
                otherCur = 0
        return max(big, sum(nums) - small) if big > 0 else max(nums)