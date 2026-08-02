class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        results = []

        cols = set()
        neg_diagonals = set()
        pos_diagonals = set()

        def backtrack(row):
            if row == n:
                solution = []

                for row_arr in board:
                    solution.append("".join(row_arr))

                results.append(solution)
                return

            for col in range(n):

                if (col in cols or row - col in neg_diagonals or row + col in pos_diagonals):
                    continue

                board[row][col] = "Q"

                cols.add(col)
                neg_diagonals.add(row - col)
                pos_diagonals.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."

                cols.remove(col)
                neg_diagonals.remove(row - col)
                pos_diagonals.remove(row + col)

        backtrack(0)
        return results