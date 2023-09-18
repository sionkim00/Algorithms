class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.nums = nums
        self.total = sum(nums)
        self.leftSum = [nums[0]]
        self.rightSum = [0] * N
        self.rightSum[N-1] = nums[N-1]

        for i in range(1,N):
            self.leftSum.append(self.leftSum[i-1] + self.nums[i])
        for i in range(N-2,-1,-1):
            self.rightSum[i] += self.rightSum[i+1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        l = 0 if left-1 < 0 else self.leftSum[left-1]
        r = 0 if right >= len(self.nums)-1 else self.rightSum[right+1]
        return self.total - l - r


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)