class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        high = 0
        asterisk = 0

        for i in s:
            if i == ")":
                high += 1
            elif i == "(":
                lo += 1
            else:
                asterisk += 1
        print(lo, high, asterisk)
        return abs(lo - high) <= asterisk