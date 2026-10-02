class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        long = 1


        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j == i:
                    continue
                elif j == i + 1:
                    dp[i][j] == s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j] and (i + j - 1) > long:
                    start = i
                    long = (i + j - 1)
        return s[start: start + long]