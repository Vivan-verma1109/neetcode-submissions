class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in s:
                    path.append(nums[i])
                    s.add(nums[i])
                    backtrack(path)
                    s.remove(nums[i])
                    path.pop()                    
        backtrack([])
        return res            
