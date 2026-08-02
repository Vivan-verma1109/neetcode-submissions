class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * (len(nums) - 1)
        arr1 = nums[:len(nums) - 1]
        dp[0] = arr1[0]
        dp[1] = max(arr1[1], arr1[0])

        for i in range(2, len(arr1)):
            dp[i] = max(dp[i - 1], arr1[i] + dp[i - 2])

        arr2 = nums[1:]
        dp1 = [0] * (len(nums) - 1)
        dp1[0] = arr2[0]
        dp1[1] = max(arr2[1], arr2[0])


        for i in range(2, len(arr2)):
            dp1[i] = max(dp1[i - 1], arr2[i] + dp1[i - 2])
        return max(dp[-1], dp1[-1])