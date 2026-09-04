class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for c in set(s):
            first = s.index(c)
            last = s.rindex(c)
            if last - first < 2:
                continue
            count += len(set(s[first+1:last]))
        return count