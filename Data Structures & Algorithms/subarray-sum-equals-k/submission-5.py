#prefix sum
# sum(i..j) = prefix[j + 1] - prefix[i]
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0
        count = {0: 1}

        for num in nums:
            prefix += num
            result += count.get(prefix - k, 0)
            count[prefix] = count.get(prefix, 0) + 1
        return result