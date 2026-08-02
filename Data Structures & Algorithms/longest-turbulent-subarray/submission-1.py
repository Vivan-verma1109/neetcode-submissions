class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        l = 0

        for r in range(1, n):
            cmp = arr[r-1] - arr[r]

            if cmp == 0:
                l = r
            elif r == n - 1 or (arr[r-1] - arr[r]) * (arr[r] - arr[r+1]) >= 0:
                ans = max(ans, r - l + 1)
                l = r

        return ans