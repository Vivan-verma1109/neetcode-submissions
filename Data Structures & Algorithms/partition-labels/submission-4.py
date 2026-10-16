class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}

        for i in range(len(s)):
            pos[s[i]] = i
        
        
        res = []

        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, pos[c])

            if i == end:
                res.append(size)
                size = 0
        return res