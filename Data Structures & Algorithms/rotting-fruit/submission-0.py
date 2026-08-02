class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if fresh == 0:
            return 0

        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
        if fresh > 0:
            return -1
        return minutes


