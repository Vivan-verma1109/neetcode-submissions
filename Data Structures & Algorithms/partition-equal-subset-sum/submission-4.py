class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        s = {0}

        for i in nums:
            t = set(s)
            for n in s:
                if n + i > target:
                    break
                t.add(n + i)
            s = t
        return target in s
