class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l <= r:
            temp = s[l:r + 1]

            if temp == temp[::-1]:
                return r - l + 1

            temp = s[l + 1:r + 1]
            if temp == temp[::-1]:
                return r - l

            temp = s[l:r]
            if temp == temp[::-1]:
                return r - l

            l += 1
            r -= 1

        return 1