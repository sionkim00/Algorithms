class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = defaultdict()
        def dp(i=0):
            elif i >= N:
                memo[i] = 0
                memo[i] = max(dp(i+1), dp(i+2) + nums[i])
        return dp()
            if i in memo:
                pass
            return memo[i]
            else:

[
