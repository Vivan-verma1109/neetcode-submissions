class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:                  # left half sorted
                if nums[l] <= target < nums[mid]:     # target inside it
                    r = mid - 1
                else:
                    l = mid + 1
            else:                                     # right half sorted
                if nums[mid] < target <= nums[r]:     # target inside it
                    l = mid + 1
                else:
                    r = mid - 1
        return -1