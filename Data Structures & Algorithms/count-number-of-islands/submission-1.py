class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def cleanup(r, c):
            if r < 0 or r >= len(grid):
                return

            if c < 0 or c >= len(grid[0]):
                return
            
            if grid[r][c] == "0" or grid[r][c] == "X":
                return
            grid[r][c] = "X"
            cleanup(r, c + 1)
            cleanup(r, c - 1)
            cleanup(r - 1, c)
            cleanup(r + 1, c)




        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    cleanup(i, j)
        
        return count


