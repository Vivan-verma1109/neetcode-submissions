class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[amount] = min ways to make said amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]