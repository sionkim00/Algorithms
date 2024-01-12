class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def vowelCount(s):
            cnt = 0
            for i in range(len(s)):
                if s[i].lower() in "aeiou":
                    cnt += 1
            return cnt
        return vowelCount(s[:len(s) // 2]) == vowelCount(s[len(s) // 2:])
"
