class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for l in range(len(s)):
            if not dp[l]:
                continue
            
            for r in range(l + 1, len(s) + 1):
                if s[l:r] in wordDict:
                    dp[r] = True
        return dp[-1]