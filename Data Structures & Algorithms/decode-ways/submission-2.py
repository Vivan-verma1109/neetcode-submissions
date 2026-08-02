class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        dp[0] = 1
        if s[0] == '0':
            dp[0] = 0
        if len(s) < 2:
            return dp[0]
            
        dp[1] = (dp[0] if s[1] != '0' else 0) + (1 if 10 <= int(s[0:2]) <= 26 else 0)

        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]