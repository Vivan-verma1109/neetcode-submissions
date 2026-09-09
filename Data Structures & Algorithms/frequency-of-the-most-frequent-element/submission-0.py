class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        maxFreq = 0
        windowSum = 0

        for right in range(len(nums)):
            windowSum += nums[right]
            while (right - left + 1) * nums[right] - windowSum > k:
                windowSum -= nums[left]
                left += 1
            maxFreq = max(maxFreq, right - left + 1)
        return maxFreq