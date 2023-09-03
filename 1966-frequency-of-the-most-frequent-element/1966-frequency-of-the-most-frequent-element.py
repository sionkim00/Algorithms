class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # need n log n solution
        nums.sort()

        l = 0
        N = len(nums)
        total = 0
        maxLen = 0
        for i in range(N):
            total += nums[i]
            if nums[i]*(i-l+1) <= total + k:
                maxLen = max(maxLen, (i-l+1))
            else:
                while nums[i]*(i-l+1) > total + k:
                    total -= nums[l]
                    l += 1
        return maxLen