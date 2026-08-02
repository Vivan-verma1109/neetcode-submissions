class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtrack(opened, close, path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            if opened < n:
                path.append("(")
                backtrack(opened + 1, close, path)
                path.pop()
            if close < opened:
                path.append(")")
                backtrack(opened, close + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
            