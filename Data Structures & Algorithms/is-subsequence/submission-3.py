class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and t:
            return True
        sp = 0
        tp = 0

        while tp < len(t):
            if sp == len(s) - 1:
                return True
            if t[tp] == s[sp]:
                sp += 1
            tp += 1
        return False
            