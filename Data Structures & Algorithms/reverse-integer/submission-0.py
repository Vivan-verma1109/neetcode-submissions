class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        s = str(x)
        s = s[::-1]
        x = int(s)
        if neg:
            x *= -1
        if x > 2**31 - 1:
            return 0
        if x < (-2**31):
            return 0
        return x