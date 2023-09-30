class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        kvp = defaultdict(int)

        for i in range(len(nums)):
            if kvp[nums[i]] >= 1:
                return True
            if i >= k:
                kvp[nums[i-k]] -= 1
            kvp[nums[i]] += 1
        return False