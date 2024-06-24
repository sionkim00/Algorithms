class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMin = prices[0]
        N = len(prices)
        res = 0

        for i in range(1, N):
            res = max(res, prices[i] - prevMin)
            prevMin = min(prevMin, prices[i])

        return res
[
