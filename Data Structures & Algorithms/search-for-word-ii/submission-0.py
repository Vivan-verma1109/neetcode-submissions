class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        s = set()
        word = set(words)

        for i in range(len(words)):
            for j in range(1, len(words[i]) + 1):
                s.add(words[i][:j])
    
        def dfs(r, c, path):
            nonlocal res
            if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0:
                return
            path += board[r][c]
            if path not in s:
                return
            
            if path in word:
                res.append(path)
                word.remove(path)
            temp = board[r][c]
            board[r][c] = "#"
            dfs(r + 1, c, path)
            dfs(r - 1, c, path)
            dfs(r, c + 1, path)
            dfs(r, c - 1, path)
            board[r][c] = temp

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, "")
        return res
