class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        kvp = defaultdict(bool)

        for num in nums:
            if num in kvp:
                return True
            kvp[num] = True
        return False
[
[1,2,3,1]
[1,2,3,4]
[1,1,1,3,3,4,3,2,4,2]
true
false
true
true
false
true
