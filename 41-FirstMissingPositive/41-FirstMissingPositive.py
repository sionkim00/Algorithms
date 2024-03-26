    def firstMissingPositive(self, nums: List[int]) 
-> int:
        s = set(nums)
        for i in range(1, len(nums) + 2):
            if not(i in s):
                return i
class Solution:
[
