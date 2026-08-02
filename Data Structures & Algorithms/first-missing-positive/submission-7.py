class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(1, max(nums)):
            if i not in s:
                return i
        if max(nums) < 0:
            return 1
        return max(nums) + 1