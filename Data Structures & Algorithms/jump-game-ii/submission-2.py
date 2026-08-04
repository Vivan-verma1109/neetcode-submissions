class Solution:
    def jump(self, nums: List[int]) -> int:
        # min ways to reach index i 
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for jump in range(1, nums[i] + 1):
                if i + jump < n:
                    dp[i + jump] = min(dp[i + jump], dp[i] + 1)

        return dp[-1]