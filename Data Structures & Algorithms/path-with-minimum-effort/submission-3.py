class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [(1,0), (0, 1), (-1, 0), (0, -1)]
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        heap = [(0, 0, 0)]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visited:
                    continue
                nDiff = abs(heights[nr][nc] - heights[r][c])
                newDiff = max(diff, nDiff)
                heapq.heappush(heap, [newDiff, nr, nc])
                