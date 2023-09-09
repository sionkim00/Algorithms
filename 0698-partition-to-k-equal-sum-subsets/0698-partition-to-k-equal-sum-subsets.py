class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        N = len(nums)
        nums.sort(reverse=True)
        visited = set()
        target = sum(nums) / k
        
        def bt(i, k, curSum):
            if k == 0:
                return True
            if curSum == target:
                return bt(0, k-1, 0)
            
            for j in range(i, N):
                if j > 0 and not ((j-1) in visited) and nums[j] == nums[j-1]:
                    continue
                if j in visited or (nums[j] + curSum > target):
                    continue
                visited.add(j)
                if bt(j+1, k, curSum + nums[j]):
                    return True
                visited.remove(j)
            return False
        
        return bt(0, k, 0)
