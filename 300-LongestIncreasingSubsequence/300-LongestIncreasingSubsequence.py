                memo[key] = 0
            elif prev >= nums[i]:
                memo[key] = dp(i+1, prev)
            else:
                memo[key] = max(dp(i+1, nums[i]) + 1, dp(i+1, 
prev))
            return memo[key]
        return dp()
            elif i >= N:
                pass
            if key in memo:
            key = (i, prev)
        def dp(i=0, prev = float("-inf")):
        memo = defaultdict()
        N = len(nums)
    def lengthOfLIS(self, nums: List[int]) -> int:
class Solution:
[
