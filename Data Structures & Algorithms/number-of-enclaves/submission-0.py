class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = [[False] * COLS for _ in range(ROWS)]
        q = deque()

        land, borderland = 0,0

        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] == 1 and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    q.append((r, c))
                    visit[r][c] = True
        
        while q:
            r, c = q.popleft()
            borderland += 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and not visit[nr][nc]):
                    q.append((nr, nc))
                    visit[nr][nc] = True
        
        return land - borderland
