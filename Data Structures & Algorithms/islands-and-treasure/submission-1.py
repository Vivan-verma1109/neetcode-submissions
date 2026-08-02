class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        print(q)

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))