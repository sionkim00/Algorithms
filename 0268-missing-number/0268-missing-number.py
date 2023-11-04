class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minNum = 0
        maxNum = 0
        total = 0

        for num in nums:
            total += num
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
        
        if minNum != 0:
            return 0
        if len(nums) > maxNum:
            return len(nums)

        tgtSum = 0
        for i in range(len(nums)+1):
            tgtSum += i
        return tgtSum - total