class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (
                    (
                        r == 0
                        or r == len(board) - 1
                        or c == 0
                        or c == len(board[0]) - 1
                    )
                    and board[r][c] == "O"
                ):
                    board[r][c] = "T"
                    q.append((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if (0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O"):
                        board[nr][nc] = "T"
                        q.append((nr, nc))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"