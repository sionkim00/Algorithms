        for i in range(len1):
            for j in range(len2):
                newI = i + 1
                newJ = j + 1

                if text1[i] == text2[j]:
                    dp[newI][newJ] = dp[newI-1][newJ-1] + 1
                else:

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        ans = 0
        len1 = len(text1)
        len2 = len(text2)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
"
