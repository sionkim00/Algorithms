    def sortedSquares(self, nums: List[int]) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            heapq.heappush(minHeap, abs(num))
        
        while minHeap:
        res = []
            cur = heapq.heappop(minHeap)
            res.append(cur ** 2)
        return res

[
