class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * (n+1)
        prices[src] = 0
        
        for i in range(k+1):
            tmpPrices = prices.copy()
            for a, b, cost in flights:
                if tmpPrices[a] == float("inf"):
                    continue
                if prices[a] + cost < tmpPrices[b]:
                    tmpPrices[b] = prices[a] + cost
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1
4
