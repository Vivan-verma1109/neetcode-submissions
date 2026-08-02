class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = max subarray to this value
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)
