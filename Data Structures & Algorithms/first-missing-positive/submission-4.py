class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if x+1 not in nums:
                return x+1
        return len(nums)+1
                