class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        prev = None
        occurrences = 0

        for r in range(len(nums)):
            val = nums[r] % 100000

            if val == prev:
                occurrences += 1
            else:
                prev = val
                occurrences = 1

            if occurrences > 2:
                nums[r] *= 100000
                count += 1

        nums.sort()
        return len(nums) - count