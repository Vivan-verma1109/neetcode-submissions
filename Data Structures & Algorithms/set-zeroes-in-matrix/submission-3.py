class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:   
        ROWS, COLS = len(matrix), len(matrix[0])

        row = any(matrix[0][c] == 0 for c in range(COLS))
        col = any(matrix[r][0] == 0 for r in range(ROWS))

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
        
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        if row:
            for c in range(COLS):
                matrix[0][c] = 0

        if col:
            for r in range(ROWS):
                matrix[r][0] = 0