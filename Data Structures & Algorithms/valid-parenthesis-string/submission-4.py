class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        high = 0

        for i in s:
            if i == "(":
                lo += 1
                high += 1
            if i == ")":
                lo -= 1
                high -= 1
            if i == "*":
                high += 1
                lo -= 1
            if high < 0:
                return False
            lo = max(0, lo)
        return lo == 0