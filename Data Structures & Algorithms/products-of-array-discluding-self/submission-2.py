class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            pre[i] = prefix
            prefix *= nums[i]
        
        suf = [1] * len(nums)
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            suf[i] = suffix
            suffix *= nums[i]
        
        res = []

        for i in range(len(nums)):
            res.append(pre[i] * suf[i])
        return res
