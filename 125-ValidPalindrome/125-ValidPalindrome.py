                l += 1
            while r >= 0 and not s[r].isalnum():
        r = len(s) - 1

        while l < r:
            while l < len(s) and not s[l].isalnum():
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
"
