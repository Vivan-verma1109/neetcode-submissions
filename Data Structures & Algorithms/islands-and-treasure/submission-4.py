class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 2147483647):
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))