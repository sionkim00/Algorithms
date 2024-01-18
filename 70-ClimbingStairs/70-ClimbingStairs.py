            elif i + 2 <= n:
                memo[i] = dp(i+1) + dp(i+2) + 1
            else:
                memo[i] = dp(i+1)
            return memo[i]
        return dp() + 1
2
