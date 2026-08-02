class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = []
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.append(val)
        for j in range(9):
            seen = []
            for i in range(9):
                val = board[i][j]
                if val != '.':
                    if val in seen:
                        return False
                    seen.append(val)
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                seen = []
                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.append(val)
        return True
        