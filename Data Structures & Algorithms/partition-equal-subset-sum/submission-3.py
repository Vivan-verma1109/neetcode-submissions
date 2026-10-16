class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        s = {0}

        for i in nums:
            t = set(s)
            for n in s:
                t.add(n + i)
            s = t
        return target in s
