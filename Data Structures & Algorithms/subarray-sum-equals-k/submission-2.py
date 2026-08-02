#prefix sum
# sum(i..j) = prefix[j + 1] - prefix[i]
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = {0: 1}
        ans = 0

        for num in nums:
            prefix += num
            if prefix - k in count:
                ans += count[prefix - k]
            if prefix in count:
                count[prefix] += 1
            else:
                count[prefix] = 1
        return ans
