class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i, path)
                    path.pop()
        backtrack(0, [])
        return (res)