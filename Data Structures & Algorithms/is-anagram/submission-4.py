class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for a, b in zip(s, t):
            if a != b:
                return False
        return True