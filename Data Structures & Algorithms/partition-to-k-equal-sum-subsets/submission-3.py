class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        if max(nums) > sum(nums) // k:
            return False
        
        nums.sort(reverse = True)
        target = sum(nums) // k

        arr = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(len(arr)):
                if arr[j] + nums[i] <= target:
                    arr[j] += nums[i]

                    if backtrack(i + 1):
                        return True
                    arr[j] -= nums[i]

                    if arr[j] == 0:
                        break

            return False
        return backtrack(0)

