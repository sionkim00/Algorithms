class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        ans = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= N or c >= M or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r, c-1) + dfs(r, c+1)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, dfs(i,j))
        return ans