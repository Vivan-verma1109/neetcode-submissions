class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        #dp[(i, s)] = count partial sum s using the first i numbers.

        def recurse(i, curr):
            if (i, curr) in dp:
                return dp[(i, curr)]

            if i == len(nums):
                return 1 if curr == target else 0
            
            dp[(i, curr)] = recurse(i + 1, curr + nums[i]) + recurse(i + 1, curr - nums[i])

            return dp[(i, curr)]
        return recurse(0, 0)