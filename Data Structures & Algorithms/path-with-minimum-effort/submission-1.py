class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1], [0, -1], [1,0], [-1,0]]
        visited = set()
        heap = [[0, 0, 0]]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            visited.add((r,c))

            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visited):
                    continue
                ndiff = abs(heights[r][c] - heights[nr][nc])
                newdiff = max(ndiff, diff)
                heapq.heappush(heap, [newdiff, nr, nc])
