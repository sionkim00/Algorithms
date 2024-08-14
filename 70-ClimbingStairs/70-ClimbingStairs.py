    def climbStairs(self, n: int) -> int:
        memo = defaultdict()
        def recur(n):
            if n in memo:
                pass
            elif n <= 2:
                memo[n] = n
            else:
                memo[n] = recur(n-1) + recur(n-2)
            return memo[n]
        return recur(n)
2
2
3
2
3
2
3
