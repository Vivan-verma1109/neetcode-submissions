class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        count = 1
        for i in range(min(nums), max(nums)):
            temp = 1
            while i in s and i + 1 in s and i < max(nums):
                temp += 1
                i += 1
                count = max(temp, count)
        return  (count)
