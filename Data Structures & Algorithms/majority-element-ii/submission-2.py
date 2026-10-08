class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        print(c)
        n = len(nums)
        for a, b in c.items():
            if b > n // 3:
                res.append(a)
        return res