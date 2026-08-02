class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #     b b b b 
        #.  a           .
        #.  a           .
        #.  a           .
        #.  a           .

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        if len(s1) + len(s2) != len(s3):
            return False

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0:
                    if dp[i-1][j] and s1[i-1] == s3[i + j - 1]:
                        dp[i][j] = True
                if j > 0:
                    if dp[i][j-1] and s2[j - 1] == s3[i + j - 1]:
                        dp[i][j] = True
        return dp[-1][-1]