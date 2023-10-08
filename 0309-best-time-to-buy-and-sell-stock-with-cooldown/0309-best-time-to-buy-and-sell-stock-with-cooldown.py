class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        memo = {}
        
        def dp(i, prev, cooldown):
            key = (i, prev, cooldown)
            if key in memo:
                pass
            elif i == N:
                memo[key] = 0
            elif cooldown:
                memo[key] = dp(i+1, prev, False)
            elif prev == -1:
                memo[key] = max(dp(i+1, prices[i], False), dp(i+1, -1, False))
            else:
                memo[key] = max(dp(i+1, -1, True) +  (prices[i]-prev), dp(i+1, prev, False))
            return memo[key]

        return dp(0, -1, False)