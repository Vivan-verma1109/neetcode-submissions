class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = Counter()
        l = 0
        best = (0, float("inf"))   # (start, length) of best window

        def valid():
            for c in need:
                if window[c] < need[c]:
                    return False
            return True

        for r in range(len(s)):
            window[s[r]] += 1                     # expand: s[r] enters

            while valid():                        # shrink while valid
                if r - l + 1 < best[1]:
                    best = (l, r - l + 1)         # record best (l, r)
                window[s[l]] -= 1                 # evict s[l]
                l += 1

        start, length = best
        return "" if length == float("inf") else s[start:start + length]