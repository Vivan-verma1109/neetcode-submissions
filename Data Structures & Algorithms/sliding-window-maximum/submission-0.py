class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_max = max(nums[:k])
        ans = [curr_max]

        l = 0

        for r in range(k, len(nums)):
            outgoing = nums[l]
            incoming = nums[r]

            if incoming > curr_max:
                curr_max = incoming
            elif outgoing == curr_max:
                curr_max = max(nums[l + 1:r + 1])

            ans.append(curr_max)
            l += 1

        return ans