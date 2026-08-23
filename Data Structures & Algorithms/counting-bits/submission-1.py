class Solution:
    def countBits(self, n: int) -> List[int]:
        #count of 1s in i = count of 1s in i // 2, plus 1 if i is odd (last bit is 1).
        #dp[i] = dp[i // 2] + (i % 2)
        dp = [0] * (n + 1)

        for i in range(n + 1):
            dp[i] = dp[i // 2] + (i % 2)
        return dp