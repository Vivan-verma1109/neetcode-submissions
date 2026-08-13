
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder in hashmap:
                if i - hashmap[remainder] > 1:
                    return True
            else:
                hashmap[remainder] = i
        return False
