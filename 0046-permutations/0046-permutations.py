class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visiting = set()
        res = []
        N = len(nums)

        def perms(arr = []):
            if len(arr) == N:
                res.append(arr)
                return
            for i in range(N):
                if not(i in visiting):
                    visiting.add(i)
                    perms([*arr, nums[i]])
                    visiting.remove(i)
        perms()
        return res