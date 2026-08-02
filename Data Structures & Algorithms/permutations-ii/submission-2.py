class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        arr = [False] * len(nums)


        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if arr[i]:
                    continue
                if i > 0 and not arr[i - 1] and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                arr[i] = True
                backtrack(path)
                arr[i] = False
                path.pop()


        backtrack([])
        return res
