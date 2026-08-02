class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in seen:
                length = 0
                val = num
                while val in seen:
                    val += 1
                    length += 1
                best = max(best, length)
        return best
