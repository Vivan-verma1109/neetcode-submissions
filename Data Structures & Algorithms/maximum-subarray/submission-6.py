class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = 0
        for i in range(1, len(nums)):
            cur += nums[i]
            best = max(best, cur)

            if cur < 0:
                cur = 0
        return best

