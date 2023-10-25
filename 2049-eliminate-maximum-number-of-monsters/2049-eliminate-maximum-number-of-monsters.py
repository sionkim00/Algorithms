class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = []
        N = len(dist)
        for i in range(N):
            minReach.append(math.ceil(dist[i] / speed[i]))
        minReach.sort()
        i = 0
        for i in range(N):
            if minReach[i] <= i:
                return i
        return i + 1