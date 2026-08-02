class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)
        s1 = list(s1)
        s1.sort()
        s1 = "".join(s1)
        s2 = list(s2)

        for i in range(len(s2) - r + 1):
            temp = s2[l:r]
            temp.sort()
            temp = "".join(temp)
            print(temp, s1)
            if temp == s1:
                return True
            l += 1
            r += 1
        return False