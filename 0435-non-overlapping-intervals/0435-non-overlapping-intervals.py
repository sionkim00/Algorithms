class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        N = len(intervals)
        res = 0

        for i in range(1, N):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return res