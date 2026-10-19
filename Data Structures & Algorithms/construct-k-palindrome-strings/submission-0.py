class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        counts = [0] * 26
        for c in s:
            counts[ord(c) - 97] += 1
        ret = 0

        for i in counts:
            ret += i % 2
        return ret <= k
