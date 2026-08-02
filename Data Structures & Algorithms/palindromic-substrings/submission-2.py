class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(l, r):
            match = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                match += 1
            return match
        
        for i in range(len(s)):

            count += expand(i, i)
            count += expand(i, i + 1)
            
        return count