class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            longest = 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]):
                    longest = max(longest, 1 + dfs(nr, nc))
                
            dp[r][c] = longest
            return longest

        
        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c))

        return ans