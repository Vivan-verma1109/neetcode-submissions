class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def function(i, j):

            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return

            if grid[i][j] == "0" or grid[i][j] == "X":
                return

            grid[i][j] = "X"
            
            function(i, j + 1)
            function(i, j - 1)
            function(i + 1, j)
            function(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # call function
                    count += 1
                    function(i, j)
        return count
        