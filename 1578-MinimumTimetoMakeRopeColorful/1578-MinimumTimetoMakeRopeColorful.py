        def dp(i, prev):
            elif i >= N:
                memo[key] = 0
            elif colors[i] == prev:
                memo[key] = dp(i+1, prev) + neededTime[i]
            else:
                memo[key] = min(dp(i+1, colors[i]), dp(i+1, None) + neededTime[i])

            key = (i, prev)
            if key in memo:
                pass
        memo = {}
            return memo[key]
        return dp(0, None)
        N = len(colors)
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
"
