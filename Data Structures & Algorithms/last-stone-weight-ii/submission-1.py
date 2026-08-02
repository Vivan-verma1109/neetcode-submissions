class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for s in range(target, stone - 1, -1):
                dp[s] = dp[s] or dp[s - stone]
        
        index = -1
        while dp[index] == False:
            index -= 1
        print(index)
        
        closest = target + 1 + index
        return total - 2 * closest
        
