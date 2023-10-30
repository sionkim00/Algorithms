class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}

        def dp(i, firstVisited):
            key = (i, firstVisited)
            if key in memo:
                pass
            elif i >= N:
                memo[key] = 0
            elif i == 0:
                memo[key] = max(dp(i+1, False), dp(i+2, True) + nums[i])
            elif i == N-1 and firstVisited:
                memo[key] = 0
            else:
                memo[key] = max(dp(i+1, firstVisited), dp(i+2, firstVisited) + nums[i])
            return memo[key]
        return dp(0, False)
