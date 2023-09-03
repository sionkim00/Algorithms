class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        N = len(cost)
        def dp(i):
            if i in memo:
                pass
            elif i >= N:
                memo[i] = 0
            else:
                memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        return min(dp(0), dp(1))