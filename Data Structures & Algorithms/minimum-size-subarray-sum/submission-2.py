class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        store = 0
        length = float("inf")

        for r in range(len(nums)):
            store += nums[r]
            while store >= target:
                length = min(length, r - l + 1)
                store -= nums[l]
                l += 1
            print(length)
        if length == float("inf"):
            return 0
        return length