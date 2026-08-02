class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums) // 3
        res = []
        for i, k in c.items():
            if k > n:
                res.append(i)
        return res