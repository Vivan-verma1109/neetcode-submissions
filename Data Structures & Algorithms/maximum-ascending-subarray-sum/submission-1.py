class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        final = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            print(prev)
            if nums[i] > prev:
                total += nums[i]
            else:
                final = max(total, final)
                total = nums[i]
            prev = nums[i]
        return max(final, total)

