class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        i = 0
        count = 0
        while i != 3:
            t = c[i]
            print(i, t)
            for j in range(t):
                nums[count] = i
                count += 1
            i += 1
