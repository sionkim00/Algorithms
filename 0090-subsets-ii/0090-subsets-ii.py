class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        s = set()
        N = len(nums)

        def perms(i=0, cur=[]):
            key = " ".join(map(str, cur))
            if not(key in s):
                ans.append(cur)
                s.add(key)
            if i == N:
                return
            newArr = cur.copy()
            newArr.append(nums[i])
            perms(i+1, newArr)
            perms(i+1, cur)
        perms()
        return ans