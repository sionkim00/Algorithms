class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        res = [""]
        ans = 0

        for word in arr:
            for r in res:
                newRes = r + word
                if len(newRes) != len(set(newRes)):
                    continue
                res.append(newRes)
                ans = max(ans, len(newRes))
        return ans
[
