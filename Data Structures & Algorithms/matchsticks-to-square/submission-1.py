class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        if max(matchsticks) > sum(matchsticks) // 4:
            return False
        matchsticks.sort(reverse = True)
        target = sum(matchsticks) // 4

        buckets = [0, 0, 0, 0]

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if buckets[j] + matchsticks[i] <= target:
                    buckets[j] += matchsticks[i]
                
                    if backtrack(i + 1):
                        return True
                
                    buckets[j] -= matchsticks[i]

            return False
        
        return backtrack(0)
        