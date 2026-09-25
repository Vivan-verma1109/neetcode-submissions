class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0] * len(piles) for _ in range(len(piles))]

        for l in range(len(piles)): 
            dp[l][l] = piles[l]
        
        for l in range(len(piles) - 1, -1, -1):
            for r in range(l + 1, len(piles)):
                dp[l][r] = max(piles[l] - dp[l+1][r], piles[r] - dp[l][r-1])
        return dp[0][-1] > 0