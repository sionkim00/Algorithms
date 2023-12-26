            elif i  == 0:
                if target > 0:
                    memo[key] = 0
                else:
                    memo[key] = 1
            else:
                res = 0
                for j in range(max(0, target - k), target):
                    res += dp(i-1, j)
            if key in memo:
                pass
        def dp(i, target):
            key = (i, target)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
1
1
