class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]

        for i in range(1, len(nums)):
            val = nums[i]

            dp[i][0] = max(dp[i-1][0] * val, dp[i-1][1] * val, val)
            dp[i][1] = min(dp[i-1][0] * val, dp[i-1][1] * val, val)
            
        res = float("-inf")
        for i in dp:
            res = max(res, i[0])
        return res