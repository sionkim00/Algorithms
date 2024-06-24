class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 1 

        for r in range(1, len(s)):
            while s[r] in s[l:r]:
                l += 1
            res = max(res, r-l+1)
        if s == "":
            return 0
            
        return res
"
