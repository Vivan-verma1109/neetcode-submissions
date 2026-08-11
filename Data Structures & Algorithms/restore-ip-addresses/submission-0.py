class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, path):
            if len(path) == 4 and start != len(s):
                return

            if start == len(s) and len(path) == 4:
                res.append(".".join(path))
                return

            if start >= len(s):
                return
                
            for i in range(start, start + 4):
                if i == start:
                    continue
                if s[start] == '0' and i - start > 1:
                    continue
                temp = int(s[start: i])
                if temp < 0 or temp > 255:
                    continue
                path.append(s[start: i])
                backtrack(i, path)
                path.pop()
        backtrack(0, [])
        return res