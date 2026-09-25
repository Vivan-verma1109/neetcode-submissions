class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j == i:
                    continue
                elif j == i + 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j] and (j - i + 1) > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]