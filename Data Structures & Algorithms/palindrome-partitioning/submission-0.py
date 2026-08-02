class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]

                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res