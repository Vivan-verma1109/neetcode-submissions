class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            temp_max = max(
                x,
                x * max_prod,
                x * min_prod
            )

            min_prod = min(
                x,
                x * max_prod,
                x * min_prod
            )

            max_prod = temp_max
            res = max(res, max_prod)

        return res