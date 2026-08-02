class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def explore(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return
            
            if grid[i][j] == "#" or grid[i][j] == "0":
                return
            
            grid[i][j] = "#"

            explore(i, j + 1)
            explore(i, j - 1)
            explore(i + 1, j)
            explore(i - 1, j)  

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    explore(i, j)
        return count