    def missingNumber(self, nums: List[int]) -> int:
class Solution:
        ans = int((N*(N+1))/2)
        N = len(nums)

        for num in nums:
            ans -= num
        return ans
        
[
