class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(start, curr_xor):
            nonlocal total
            total += curr_xor

            for i in range(start, len(nums)):
                backtrack(i + 1, curr_xor ^ nums[i])

        backtrack(0, 0)
        return total