
        for num in nums:
            kvp[num] += 1
        kvp = dict(sorted(kvp.items(), key=lambda x: (x[1], -x[0])))

        res = []

        for key in kvp:
            for i in range(kvp[key]):
        kvp = defaultdict(int)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
[
