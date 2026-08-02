class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True
        reachable_count = 0
        
        for j in range(1, len(s)):
            enter = j - minJump
            if enter >= 0 and dp[enter]:
                reachable_count += 1
            leave = j - maxJump - 1
            if leave >= 0 and dp[leave]:
                reachable_count -= 1

            dp[j] = reachable_count > 0 and s[j] == '0'
        return dp[-1]