class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        
        def canSplit(mid):
            subarray = 1
            cur = 0
            for num in nums:
                cur += num
                if cur > mid:
                    subarray += 1
                    cur = num
                    if subarray > k:
                        return False
            return True

        res = r

        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res