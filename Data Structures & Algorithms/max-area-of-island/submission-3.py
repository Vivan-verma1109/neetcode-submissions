class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def cleanup (r, c):
            if r < 0 or r >= len(grid):
                return 0

            if c < 0 or c >= len(grid[0]):
                return 0

            if grid[r][c] == 0 or grid[r][c] == 2:
                return 0

            grid[r][c] = 2
            
            area = 1
            area += cleanup(r, c + 1)
            area += cleanup(r, c - 1)
            area += cleanup(r - 1, c)
            area += cleanup(r + 1, c)
            return area
        

        area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max (area, cleanup(i, j))

        return area



