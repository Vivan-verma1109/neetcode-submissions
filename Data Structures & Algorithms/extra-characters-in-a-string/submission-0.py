class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)
        n = len(s)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i+1]
            for word in dictionary:
                if word == s[i: i + len(word)]:
                    dp[i] = min(dp[i], dp[i + len(word)])
        return dp[0]
