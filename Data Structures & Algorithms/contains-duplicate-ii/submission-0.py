class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pairs = []

        for i in range(len(nums)):
            pairs.append((nums[i], i))

        pairs.sort()
        for i in range(1, len(pairs)):
            if pairs[i][0] == pairs[i-1][0]:
                if abs(pairs[i][1] - pairs[i-1][1]) <= k:
                    return True
        return False