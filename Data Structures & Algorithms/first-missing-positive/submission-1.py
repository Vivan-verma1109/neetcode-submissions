class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        print(s)
        for i in range(1, len(nums) + 1):
            print(i)
            if i not in s:
                return(i)
        return len(nums) + 1
                