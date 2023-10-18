class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0

        while right < len(nums):
            while left < right and nums[left] != 0:
                left += 1
                
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            while left < right and nums[left] != 0:
                left += 1
            right += 1
        print(nums)