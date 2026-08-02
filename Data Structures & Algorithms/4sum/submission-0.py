class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if total_sum == target:
                        s.add(tuple([nums[i], nums[j], nums[k], nums[l]]))
                        k += 1
                        l -= 1
                    elif total_sum < target:
                        k += 1
                    elif total_sum > target:
                        l -= 1
        return list(s)

            

