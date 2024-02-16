            freq, key = heapq.heappop(minHeap)
            if freq > k:
                heapq.heappush(minHeap, [freq-k, key])
            heapq.heappush(minHeap, [kvp[key], key])
        while k > 0:
        
        for key in kvp:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minHeap = []
        kvp = defaultdict(int)
        heapq.heapify(minHeap)

        for e in arr:
            kvp[e] += 1
[
