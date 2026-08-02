class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        print(counts)

        for i in range(len(s2) - len(s1) + 1):
            c = Counter(s2[i: i + len(s1)])
            print(c)
            if c == counts:
                return True
        return False
