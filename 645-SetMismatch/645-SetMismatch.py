class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = [0,0]
        
        for i in range(1, len(nums)+1):
            if freq[i] == 0:
                res[1] = i
            if freq[i] == 2:
                res[0] = i
        return res
[
