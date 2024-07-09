class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = 0
        ans = 0

        for arrival, time in customers:
            curTime = max(curTime, arrival)
            curTime += time
            ans += curTime - arrival
        return float(ans) / len(customers)
[
