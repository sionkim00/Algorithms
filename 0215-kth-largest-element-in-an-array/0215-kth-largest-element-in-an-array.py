class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kvp = defaultdict(int)
        for num in nums:
            kvp[num] += 1
        
        for i in range(10**4, -1*10**4-1, -1):
            if i in kvp:
                k -= kvp[i]
            if k <= 0:
                return i