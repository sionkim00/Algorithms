class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabets = [0] * 26

        for i in range(len(s)):
            alphabets[ord(s[i]) - ord('a')] += 1
            alphabets[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
        res = 0
            if alphabets[i] > 0:
                res += alphabets[i]
        return res
"
