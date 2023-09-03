class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(r=0, c=0):
            key = (r,c)
            if key in memo:
                pass
            elif r >= m or c >= n:
                memo[key] = 0
            elif r == m-1 and c == n-1:
                memo[key] = 1
            else:
                memo[key] = dp(r+1, c) + dp(r, c+1)

            return memo[key]
        
        return dp()
        