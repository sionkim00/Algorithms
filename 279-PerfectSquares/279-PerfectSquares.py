            if n in memo:
        def dp(n):
                pass
            elif n == 0:
                memo[n] = 0
                min_squares = float("inf")

                i = 1
                while i * i <= n:
                    min_squares = min(min_squares, dp(n - i * i) + 1)
                    i += 1
                memo[n] = min_squares

        memo = defaultdict()
            else:
            return memo[n]
        return dp(n)
1
