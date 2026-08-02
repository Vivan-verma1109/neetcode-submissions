class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            if (r,c) in visited:
                return
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visited)
        # Pacific: top row
        for c in range(cols):
            dfs(0, c, pacific)

        # Pacific: left column
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: bottom row
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Atlantic: right column
        for r in range(rows):
            dfs(r, cols - 1, atlantic)
        
        ans = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i,j])
        return ans

