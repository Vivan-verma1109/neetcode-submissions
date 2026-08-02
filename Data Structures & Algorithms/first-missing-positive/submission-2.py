class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        need = 1
        for i in nums:
            if i == need:
                need += 1
        return need
                