class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        while start * start < x:
            if start * start > x:
                start -= 1
            if start * start < x:
                start += 1
        if start * start > x:
            return start - 1
        return start