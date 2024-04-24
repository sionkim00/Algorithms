class Solution:
    def tribonacci(self, n: int) -> int:
        prev = [0, 1, 1]

        for i in range(3, n+1):
            prev.append(prev[-1] + prev[-2] + prev[-3])
        return prev[n]
4
