class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        for ch in s:
            c[ch] = 0

        l = 0
        length = 0

        for i in range(len(s)):
            if c[s[i]] > 0:
                while s[l] != s[i]:
                    c[s[l]] = 0
                    l += 1
                c[s[l]] = 0
                l += 1

            c[s[i]] = 1
            length = max(length, i - l + 1)

        return length