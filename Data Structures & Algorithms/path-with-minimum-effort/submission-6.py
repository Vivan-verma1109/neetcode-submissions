class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(0, 0, 0)] # (effort, row, col)
        visited = set()

        while heap:
            effort, row, col = heapq.heappop(heap)

            if (row, col) in visited:
                continue
            
            if (row, col) == (rows - 1, cols - 1):
                return effort
            
            visited.add((row, col))

            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and (nr, nc) not in visited:

                    new = max(effort, abs(heights[nr][nc] - heights[row][col]))

                    heapq.heappush((new, nr, nc))




