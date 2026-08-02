class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if board[i][j] != "O":
                return

            board[i][j] = "S"

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)


        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)

        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
