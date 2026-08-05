class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            if i >= ROWS or i < 0 or j >= COLS or j < 0:
                return
            if grid[i][j] == "0" or grid[i][j] == "#":
                return
            grid[i][j] = "#"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
 

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count