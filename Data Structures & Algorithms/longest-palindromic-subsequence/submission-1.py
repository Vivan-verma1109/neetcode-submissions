class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        res = 0
        for i in dp:
            temp = max(i)
            res = max(temp, res)
        return res

