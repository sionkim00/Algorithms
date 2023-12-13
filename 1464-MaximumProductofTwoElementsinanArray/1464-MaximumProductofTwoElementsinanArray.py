    def maxProduct(self, nums: List[int]) -> int:
        prevMax = 1

        for i in range(len(nums)):
        res = 0
            res = max(res, prevMax * (nums[i]-1))
            prevMax = max(prevMax, nums[i]-1)
        return res
[
