            elif r == N - 1:
                memo[key] = grid[r][c1] + grid[r][c2]
            elif c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == M:
                memo[key] = 0
                pass
            else:
                memo[key] = 0
                for c1_d in [-1, 0, 1]:
                    for c2_d in [-1, 0, 1]:
                        memo[key] = max(memo[key], dp(r+1, c1+c1_d, c2+c2_d))
                memo[key] += grid[r][c1] + grid[r][c2]
            return memo[key]
        return dp(0, 0, M - 1)
[
