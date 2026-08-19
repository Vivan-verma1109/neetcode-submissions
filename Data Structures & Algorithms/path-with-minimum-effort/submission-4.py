class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]

        while heap:
            effort, i, j = heapq.heappop(heap)

            if effort > dist[i][j]:
                continue

            for dr, dc in dirs:
                nr = i + dr
                nc = j + dc

                if nr < 0 or nc < 0 or nr == rows or nc == cols: 
                    continue
                new_effort = max(effort, abs(heights[nr][nc] - heights[i][j]))
                if new_effort < dist[nr][nc]:
                    heapq.heappush(heap, (new_effort, nr, nc))
                    dist[nr][nc] = new_effort
        return dist[rows-1][cols-1]