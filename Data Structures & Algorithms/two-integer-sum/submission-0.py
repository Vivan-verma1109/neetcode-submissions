class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            if target-num in s:
                return [s[target-num], i]
            else:
                s[num] = i
        